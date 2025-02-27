from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .models import CustomUser
from .serializers import CustomUserSerializer, SignInUserSerializer, SignUpUserSerializer


class CreateUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpUserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class SignInUserView(APIView):
    permission_classes = [AllowAny]
    """
    View for signing in the user.
    """

    def post(self, request):
        serializer = SignInUserSerializer(data=request.data)

        # Generating the token with SimpleJWT
        if serializer.is_valid():
            user = serializer.validated_data
            token = RefreshToken.for_user(user)

            response = Response(
                status=status.HTTP_200_OK,
            )

            response.set_cookie("access_token", str(token.access_token), httponly=True, secure=True, samesite="Strict")
            response.set_cookie("refresh_token", str(token), httponly=True, secure=True, samesite="Strict")

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignOutUserView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response


class CookieRefreshTokenView(TokenRefreshView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"error": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response(status=status.HTTP_200_OK)
            response.set_cookie("access_token", access_token, httponly=True, secure=True, samesite="Strict")
            return response
        except InvalidToken:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
