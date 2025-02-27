from django.urls import path

from .views import CookieRefreshTokenView, CreateUserView, SignInUserView, SignOutUserView, UserDetailView

urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("signin/", SignInUserView.as_view(), name="signin"),
    path("signout/", SignOutUserView.as_view(), name="signout"),
    path("refresh/", CookieRefreshTokenView.as_view(), name="refresh-token"),
    path("users/info/", UserDetailView.as_view(), name="user_detail"),
]
