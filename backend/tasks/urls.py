from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.index, name="tasks"),
    path("tasks/<int:id>/", views.details, name="task-details"),
]
