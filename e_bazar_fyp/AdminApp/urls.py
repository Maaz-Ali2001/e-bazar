from django.urls import path

from .views import Verification

obj= Verification()
urlpatterns = [
    path('', obj.home, name='home'),
    # path('verify',views.verify,name="verify")
]