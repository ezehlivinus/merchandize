from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BillSerializer, BrandSerializer, CategorySerializer, CompanySerializer, CustomerSerializer, PurchaseBookSerializer, PurchasesSerializer, SalesBookSerializer, SupplierSerializer, UserSerializer, ProductSerializer

from .models import Bill, Company, Customer, Product, Brand, Category, PurchaseBook, SalesBook, Supplier

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


# class PurchaseBookViewSet(viewsets.ModelViewSet):
#     queryset = PurchaseBook.objects.all()
#     serializer_class = PurchaseBookSerializer
    

class BillViewSet(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def post(self, request, *args, **kwargs):
        serializer = BillSerializer( data=request.data.get('bill'))

        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class CreatePurchaseBook(generics.ListCreateAPIView ):
    '''
    Purchase Book endpoint to allow the list and create of a Purchase
    In the future: This will support multiple/bulk operation
    A single purchase/invoice can have many 
    Summation of amount is/should be done at the frontend credit/debit
    '''
    queryset = PurchaseBook.objects.all()
    serializer_class = PurchaseBookSerializer

    def post(self, request, *args, **kwargs):
        # create a bill
        bill = BillViewSet.post(BillViewSet, request, *args, **kwargs)

        data = {
            'bill': bill.get('id'),
            **request.data.get('purchase_book'),
        }

        serializer = PurchaseBookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # we may want to revert changes to create bill if this is the first time of creating bill
                # Can be done later
                
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        # create purchases
        # return CreatePurchases.post(CreatePurchases, request, purchase_book)
        
        return purchase_book
                                                
# import requests
class CreatePurchases(generics.ListCreateAPIView):
    '''
    A purchases has many purchaseBook/Legder
    There is alway a single purchase/record for a PurchaseBook
    This is records sum(amount) of the items in a single PurchaseBook/Invoice
    '''
    serializer_class = PurchasesSerializer

    def post(self, request, purchase_book):
        purchase_book = purchase_book.data
        purchases = request.data

        data = {
            'particular': purchase_book.get('supplier'),
            'invoice': purchase_book.get('invoice'),
            'date': purchases.get('date'),
            # This values should be send from form by the client
            'debit': purchases.get('total', 0),
            'credit': purchases.get('total', 0)
        }

        serializer = PurchasesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SalesBookViewSet(viewsets.ModelViewSet):
    queryset = SalesBook.objects.all()
    serializer_class = SalesBookSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# class PurchasesViewSet(viewsets.ModelViewSet):
#     queryset = Purc

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

