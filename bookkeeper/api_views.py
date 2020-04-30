from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BillSerializer, BrandSerializer, CategorySerializer, BusinessSerializer, CustomerSerializer, InvoiceSerializer, PurchaseBookSerializer, PurchasesSerializer, SalesBookSerializer, SalesSerializer, SupplierSerializer, UserSerializer, ProductSerializer

from .models import Bill, Business, Customer, Invoice, Product, Brand, Category, PurchaseBook, Purchases, Sales, SalesBook, Supplier



class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


# class PurchaseBookViewSet(viewsets.ModelViewSet):
#     queryset = PurchaseBook.objects.all()
#     serializer_class = PurchaseBookSerializer
    

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def post(self, request, *args, **kwargs):
        serializer = BillSerializer( data=request.data.get('bill'))

        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        # return super().post(request, *args, **kwargs)


class PurchaseBookList(generics.ListCreateAPIView):
    '''
    \n
    Use this endpoint to list or create of a Purchase\n
    In the future: This will support multiple/bulk operation\n\n
    A single purchase/invoice can have many purchase book\n
    Summation of amount is/should be done at the frontend credit/debit for purchases endpoint
    \n
    '''
    queryset = PurchaseBook.objects.all()
    serializer_class = PurchaseBookSerializer


class PurchaseBookDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Endpoint that allow: update, detail, and delete of self resource
    '''
    queryset = PurchaseBook.objects.all()
    serializer_class = PurchaseBookSerializer
    
                                                
class PurchasesList(generics.ListCreateAPIView):
    '''
    A purchases has many purchaseBook/Legder
    There is alway a single purchase/record for a PurchaseBook
    This is records sum(amount) of the items in a single PurchaseBook/Invoice
    '''
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


class PurchasesDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Endpoint that allow: update, detail, and delete of self resource
    '''
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


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

