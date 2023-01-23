from django.urls import path
from .views import Customer
customer=Customer()
urlpatterns = [

    path('', customer.renHomePage, name="logIn"),
    path('detail/<str:product_id>/', customer.productdetail, name='productdetails'),
    path('details/<str:product_id>/', customer.productdetail, name='productvardetail'),
    path('cart/',customer.add_to_cart,name='cart'),
    path('order/',customer.order,name='order'),
    path('register/',customer.register,name='register'),

]