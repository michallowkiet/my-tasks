from . import views
from django.urls import path

urlpatterns = [
    path("tasks/", views.index, name="task-index"),
]
