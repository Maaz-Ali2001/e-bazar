
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("sellercenter/", include("Vendor.urls")),
    path('admin/', admin.site.urls),
]
