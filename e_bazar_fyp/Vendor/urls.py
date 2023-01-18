from django.urls import path
from .views import vendorRegister,Product,Category

vendor= vendorRegister()
product=Product()
categories=Category()
urlpatterns = [
    path('login/', vendor.logIn, name="logIn"),
    path('register/',vendor.register,name="register"),
    path('addproduct/',product.renselectCat,name="addproduct"),
    path('selectcategory1/',product.selectCat,name="selectcategory"),
    path('selectcategory2/',product.selectSubCat,name="selectsubcategory"),
    path('selectcategory3/',product.selectLeafCat,name="leafcat"),
    path('addpro/',product.renAddProduct,name="addpro")
]