from http.client import HTTPResponse
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
def index(request):
    return JsonResponse({"message": "Hello, world. You're at the polls index."})
