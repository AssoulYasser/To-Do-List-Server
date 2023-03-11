from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response


def home(request):
    return HttpResponse('working ..')


class TaskApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
