
from django.urls import path
from app.views import create, home, delete
urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('delete/',delete,name='delete'),
]
