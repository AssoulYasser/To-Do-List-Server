from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from .serializers import *
from .models import *
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

    def get(self, request):
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        if data:
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def put(self, request):
        id = request.data['id']
        try:
            oldData = Task.objects.get(id=id)
        except:
            return Response(status=400)

        serializer = TaskSerializer(oldData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=400)

    def delete(self, request):
        id = request.query_params.get('id')

        try:
            data = Task.objects.get(id=id)
            data.delete()
            return Response(status=200)
        except:
            return Response({"error": "NotFound"}, status=400)
