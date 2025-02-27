from django.urls import path

from .views import CreateUserView, UserDetailView

urlpatterns = [
    path("users/", CreateUserView.as_view(), name="create_user"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]
