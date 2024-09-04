from django.urls import path
from .views import *

urlpatterns = [
    path('team/', team, name='team'),
    path('bodies/', bodies, name='bodies'),
    path('body/<int:id>', body, name='body'),
    path('', home, name='home'),
]