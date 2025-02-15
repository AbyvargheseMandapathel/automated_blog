from django.urls import path
from authentication.views import *


urlpatterns = [
    path('', login_view, name='login_view'),
    
]