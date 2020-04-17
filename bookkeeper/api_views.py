from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BrandSerializer, CategorySerializer, CompanySerializer, CustomerSerializer, PurchaseBookSerializer, SalesBookSerializer, UserSerializer, ProductSerializer

from .models import Company, Customer, Product, Brand, Category, PurchaseBook, SalesBook

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PurchaseBookViewSet(viewsets.ModelViewSet):
    queryset = PurchaseBook.objects.all()
    serializer_class = PurchaseBookSerializer


class SalesBookViewSet(viewsets.ModelViewSet):
    queryset = SalesBook.objects.all()
    serializer_class = SalesBookSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

