from django.urls import path,include
from .views import *
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name = 'index'),
    path('ipo/', ipo, name = 'ipo'),
]
