
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer, userinfoSerializer
from .models import userinfo
from rest_framework.response import Response

class loginAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "Message": "User created sucessfully",
                "User" : serializer.data}, status = status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class userList (APIView):

    def get(self,request):
        userList = userinfo.objects.all()
        serializer = userinfoSerializer(userList,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer= userinfoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
