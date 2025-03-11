from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


# Create your views here.
@api_view(["GET"])
def index(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True, fields=["id", "title", "due_date"])
    return Response(serializer.data)


@api_view(["GET"])
def details(request, id: int):
    task = get_object_or_404(Task, pk=id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)
