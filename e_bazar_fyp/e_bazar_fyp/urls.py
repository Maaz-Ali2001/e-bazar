
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("sellercenter/", include("e_bazar_app.urls")),
    path('admin/', admin.site.urls),
]
