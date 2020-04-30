from django.contrib.auth.models import User

from rest_framework import serializers
from .models import (
    Bill, Customer, Invoice, Product, Category,
    Brand, Business, PurchaseBook,
    Purchases, Sales, SalesBook, Supplier
)


class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = '__all__'


class PurchasesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchases
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class SalesBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesBook
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'


class PurchaseBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseBook
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    purchase_books = PurchaseBookSerializer(many=True, read_only=True)
    purchases = PurchasesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bill 
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # When fecting Categories, also fetch related products
    products = ProductSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['username'])
            user.save()

            return user