from unicodedata import name
from django.urls import path
from . import views 

app_name = 'Django_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('listview', views.list_view, name='listview'),
    path('listview/<id>', views.detail_view, name='listview/<id>' ),
    path('listview/<id>/update', views.update_view, name='updateview'),
    path('listview/<id>/delete', views.delete_view, name='deleteview' )
]