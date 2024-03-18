from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token


# Create your views here.

# Function-based view
def home(request):
    return HttpResponse('<h1>Welcome to our Car site.</h1>')

# Class-based view
class RegistrationAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.get(username=username,password=password)
        auth.authenticate(username=username,password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            serializer = TokenSerializer(token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"User does'nt exist."}, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutAPIView(APIView):
    def post(self, request):
        pass

class CarListAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CarPostAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CarGetAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, pk):
        instance = Car.objects.get(pk=pk)
        serializer = CarSerializer(instance)
        return Response(serializer.data)
    
class CarPutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            instance = Car.objects.get(pk=pk)
            serializer = CarSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CarDeleteAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            instance = Car.objects.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BrandListAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BrandPostAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BrandGetAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, pk):
        instance = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(instance)
        return Response(serializer.data)
    
class BrandPutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            instance = Brand.objects.get(pk=pk)
            serializer = BrandSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BrandDeleteAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            instance = Brand.objects.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CarsByBrandAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, pk):
        brand = Brand.objects.get(pk=pk)
        cars = brand.Cars.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializerd.data, status=status.HTTP_200_OK)
    
