from django.db import models

# Create your models here.

class Category(models.Model):
    '''
    This describes a product's category
    Examples: Phone, Accessories, Electronics
    A category has_many Products
    '''
    name = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(max_length=200, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    '''
    This describes the brand/vendor a product belongs to
    Example: Tecno
    A brand has_many products
    '''
    name = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    '''
    This describes a product or good: an item for sale
    A product belongsTo category, brand
    '''
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100, help_text='This the model number of this product')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    '''
    This describes inventory:
    tracks the records of products sold or purchased
    '''
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # customer = 
    pass


class PurchaseBook(models.Model):
    '''
    This decsribes a purchase: a record of an item (to be resale) bought from a supplier
    But on credit
    Purchases source documents: Stock-In
    '''
    supplier = models.ForeignKey('Company', on_delete=models.CASCADE)
    invoice = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cost = models.PositiveIntegerField(default=0, help_text='This is the cost of a single product')
    amount = models.PositiveIntegerField(default=0, help_text='This is the sum of all the nuit_price')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SalesBook(models.Model):
    '''
    This describes a sale: record of credit sales to customer
    Defines Point of Sale : Sales scource documents - invoice
    '''
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, help_text='This is the quantity sold')
    price = models.PositiveIntegerField(default=0, help_text='This is the selling')
    amount = models.PositiveIntegerField(default=0)



# class PurchaseBook(models.Model):

#     purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
#     total = models.PositiveIntegerField(default=0)


class Company(models.Model):
    '''This describes a company (business)'''
    name = models.CharField(max_length=200)
    description = models.CharField(null=True, max_length=50)
    address = models.CharField(max_length=50)
    # owner = models.ForeignKey('Supplier', verbose_name='', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'


class Sale(models.Model):
    '''This describes a sale: an item sold to a customer'''
    pass


class Customer(models.Model):
    '''This describes a customer: a buyer who buys product(s)'''
    name = models.CharField(max_length=200)
    description = models.CharField(null=True, max_length=50)
    address = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Supplier(models.Model):
#     '''This describes a supplier: one whom a company buys products from'''
#     name = models.CharField(max_length=50)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



