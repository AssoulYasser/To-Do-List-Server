import traceback
from datetime import timedelta

import jwt
from django.http import HttpResponse, QueryDict
from jwt import InvalidSignatureError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *


def home(request):
    return HttpResponse('working ..')


def getUser(token: str):
    if not token:
        return Response({"ERROR": "NO TOKEN PASSED"}, status=400)
    try:
        payload = jwt.decode(token, 'secretkey', algorithms=['HS256'])
    except InvalidSignatureError:
        return Response({"ERROR": "TOKEN HAS EXPIRED"}, status=400)

    username = payload['username']
    return username


class TaskApiView(APIView):
    def post(self, request):
        username = getUser(request.headers.get('Authorization'))
        user = User.objects.get(username=username)
        received = request.data
        data = QueryDict(mutable=True)
        data.update(received)
        data.update({'user': user})
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def get(self, request):
        try:
            username = getUser(request.headers.get('Authorization'))
            user = User.objects.get(username=username)
            tasks = Task.objects.filter(user=user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"ERROR": str(e)})

    def put(self, request):
        try:
            id = request.data['id']

            username = getUser(request.headers.get('Authorization'))
            user = User.objects.get(username=username)

            received = request.data
            data = QueryDict(mutable=True)

            data.update(received)
            data.update({'user': user})

            task = Task.objects.filter(user=user, id=id).first()
            if task:
                serializer = TaskSerializer(task, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=200)
            else:
                return Response({"ERROR": "NO TASK FOUND"})

        except Exception as e:
            return Response({"ERROR": str(e)})

    def delete(self, request):
        try:
            id = request.data['id']

            username = getUser(request.headers.get('Authorization'))
            user = User.objects.get(username=username)

            received = request.data
            data = QueryDict(mutable=True)

            data.update(received)
            data.update({'user': user})

            task = Task.objects.filter(user=user, id=id).first()

            if task:
                task.delete()
                return Response(status=200)
            else:
                return Response({"ERROR": "NO TASK FOUND"})

        except Exception as e:
            return Response({"ERROR": str(e)})


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
