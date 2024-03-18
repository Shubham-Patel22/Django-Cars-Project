from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('Register', RegistrationAPIView.as_view(),name='Register-user'),
    path('Login',LoginAPIView.as_view(),name='Login-user'),
    path('api-token-auth/', auth_views.obtain_auth_token, name='auth-token'),
    path('Cars/List',CarListAPIView.as_view(),name = 'Get-all-cars-list'),
    path('Cars/Add',CarPostAPIView.as_view(),name = 'Add-car'),
    path('Cars/Show/<int:pk>',CarGetAPIView.as_view(),name = 'Show-a-single-car'),
    path('Cars/Update/<int:pk>',CarPutAPIView.as_view(),name = 'Update-car'),
    path('Cars/Delete/<int:pk>',CarDeleteAPIView.as_view(),name = 'Remove-car'),
    path('Brands/List',BrandListAPIView.as_view(),name = 'Get-all-Brands-list'),
    path('Brands/Add',BrandPostAPIView.as_view(),name = 'Add-Brand'),
    path('Brands/Show/<str:pk>',BrandGetAPIView.as_view(),name = 'Show-a-single-Brand'),
    path('Brands/Update/<str:pk>',BrandPutAPIView.as_view(),name = 'Update-Brand'),
    path('Brands/Delete/<str:pk>',BrandDeleteAPIView.as_view(),name = 'Remove-Brand'),
    path('Brands/<str:pk>/Cars', CarsByBrandAPIView.as_view(), name='Show-Cars-by-Brand'),
]
