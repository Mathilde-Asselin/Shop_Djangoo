from unicodedata import name
from django.urls import path
from . import views 

app_name = 'Shop_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/update', views.update, name='update'),
]