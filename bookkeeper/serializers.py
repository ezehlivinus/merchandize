from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Customer, Product, Category, Brand, Company, PurchaseBook, SalesBook


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class SalesBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesBook
        fields = '__all__'


class PurchaseBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseBook
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
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