from rest_framework.response import Response
from rest_framework import viewsets
from UserApp.models import User
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])  # This is a decorator
# def getData(request):
#     (userArray, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def postData(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)