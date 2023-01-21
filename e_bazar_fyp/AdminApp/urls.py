from django.urls import path

from .views import Verification

obj= Verification()
urlpatterns = [
    path('', obj.home, name='home'),
    path('statuschange/<str:status_type>', obj.status_change, name='status_change'),
    # path('verify',views.verify,name="verify")
]