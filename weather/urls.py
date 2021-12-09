from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path(r'<city_id>/del', views.del_city, name='del_view'),
]
