from django.urls import path

from .views import CreateUserView, SignInUserView, UserDetailView

urlpatterns = [
    path("users/signup", CreateUserView.as_view(), name="signup"),
    path("users/signin", SignInUserView.as_view(), name="signin"),
    path("users/info/", UserDetailView.as_view(), name="user_detail"),
]
