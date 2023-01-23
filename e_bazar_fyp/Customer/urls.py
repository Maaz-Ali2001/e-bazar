from django.urls import path
from .views import Customer
customer=Customer()
urlpatterns = [
    path('', customer.renHomePage, name="logIn"),
    path('cart/',customer.add_to_cart,name='cart'),
    path('<str:product_id>/',customer.productdetail,name='productdetail'),
    path('<str:id>/',customer.productdetail,name='productvardetail'),
    path('order/',customer.order,name='order'),
    path('register/',customer.register,name='register'),

]