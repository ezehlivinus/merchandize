from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from .api_views import  BillViewSet, BrandViewSet, CategoryViewSet, CompanyViewSet, CreatePurchaseBook, CustomerViewSet, ProductViewSet, SalesBookViewSet, SupplierViewSet, UserCreate

router = DefaultRouter()
router = DefaultRouter(trailing_slash=False)


router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('brands', BrandViewSet, basename='brands')
router.register('companies', CompanyViewSet, basename='companies')
# router.register('purchases', PurchaseBookViewSet, basename='purchases')
router.register('customers', CustomerViewSet, basename='customers')
router.register('sales', SalesBookViewSet, basename='sales')
router.register('suppliers', SupplierViewSet, basename='suppleirs')
# router.register('bills', BillViewSet, basename='bills')



schema_view = get_swagger_view(title='Bookeeping API')

urlpatterns = [
    url(r'', include(router.urls)),
    path('purchases', CreatePurchaseBook.as_view(), name='purchases'),
    # path('categories/<int:cat_id>/brands/<int:brand_id>/products', ProductViewSet.as_view({'post': 'create', 'get': 'list', 'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('bills', BillViewSet.as_view(), name='bills'),
    path('docs', include_docs_urls(title='Bookkeeping API')),
    path('swagger-docs', schema_view),
    # path('users/', UserCreate.as_view(), name='user_create'),
    # path('users/', UserCreate.as_view(), name='user_create'),
]