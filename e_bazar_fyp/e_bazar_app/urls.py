from django.urls import path
from .views import vendorRegister,Product,Category

vendor= vendorRegister()
product=Product()
categories=Category()
urlpatterns = [
    path('', vendor.logIn, name="logIn"),
    path('register',vendor.register,name="register"),
    path('addproduct',product.renselectCat,name="addproduct"),
    path('selectcategory',product.selectCat,name="selectcategory"),
    path('<str:parent>',product.selectSubCat,name="selectsubcategory"),
    path('<str:subparent>',product.selectLeafCat,name="selectleafcategory")

]