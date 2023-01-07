
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("Signup/", include("e_bazar_app.urls")),
    path('admin/', admin.site.urls),
]
