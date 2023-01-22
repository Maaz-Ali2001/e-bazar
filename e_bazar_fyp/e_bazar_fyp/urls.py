
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("sellercenter/", include("Vendor.urls")),
    path("administrator/",include("AdminApp.urls")),
    path('customer/',include("Customer.urls")),
    path('admin/', admin.site.urls),

]
