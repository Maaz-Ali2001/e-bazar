from django.urls import path
from .views import Customer
customer=Customer()
urlpatterns = [
    path('', customer.renHomePage, name="logIn"),
    path('<str:product_id>/',customer.productdetail,name='productdetail'),
    path('cart/',customer.add_to_cart,name='cart'),
    path('<str:id>/',customer.productVarDetail,name='productvardetail')

]