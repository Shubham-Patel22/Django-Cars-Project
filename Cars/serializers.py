# Cars/serializers.py

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    #Adding this line is breaking the POST API of car.
    #brand = BrandSerializer()

    class Meta:
        model = Car
        fields = '__all__'
    
    '''def create(self, validated_data):
        # Extract Brand data from validated data
        brand_data = validated_data.pop('brand')
        brand_name = brand_data['brand_name']
        #brand = Brand.objects.get(brand_name=brand_name)
        print(brand)
        if brand is None:
            brand_serializer = BrandSerializer(data=brand_data)
        if brand_serializer.is_valid():
            brand = brand_serializer.save()
        else:
            raise serializers.ValidationError(brand_serializer.errors)

        brand, created = Brand.objects.get_or_create(brand_name=brand_name)
        if not created:
            for key, value in parent_data.items():
                setattr(parent, key, value)
            brand.save()

        # Associate Brand with Car and create Car record
        validated_data['brand'] = brand
        car = Car.objects.create(**validated_data)
        car['brand'] = brand
        car.save()
        return car'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

'''class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'''