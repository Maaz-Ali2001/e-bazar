from django.urls import path
from .views import Customer
customer=Customer()
urlpatterns = [
    path('', customer.renHomePage, name="logIn"),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('cart/',customer.add_to_cart,name='cart'),
    path('<str:product_id>/',customer.productdetail,name='productdetail'),
    path('<str:id>/',customer.productdetail,name='productvardetail'),



=======
    path('productdetail/',customer.productdetail,name='productdetail'),
    path('cart/',customer.add_to_cart,name='cart')
>>>>>>> parent of dc9a9c5 (cart done)
=======
    path('productdetail/',customer.productdetail,name='productdetail'),
    path('cart/',customer.add_to_cart,name='cart')
>>>>>>> parent of dc9a9c5 (cart done)
=======
    path('productdetail/',customer.productdetail,name='productdetail'),
    path('cart/',customer.add_to_cart,name='cart')
>>>>>>> parent of dc9a9c5 (cart done)
]