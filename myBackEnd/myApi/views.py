import traceback
from datetime import timedelta

import jwt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *


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


class UserSignInApiView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({"ERROR": "USER NOT FOUND"}, status=400)

        if not user.check_password(password):
            return Response({"ERROR": "WRONG PASSWORD"}, status=400)

        payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(minutes=10),
            'iat': datetime.utcnow()
        }

        token = jwt.encode(payload, 'secretkey', algorithm='HS256')

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {"token": token, 'username': username}

        return response


class UserSignUpApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
