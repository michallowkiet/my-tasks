from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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
            return Response(
                {
                    "refresh": str(token),
                    "access": str(token.access_token),
                }
            )
        return Response(serializer.errors, status=400)
