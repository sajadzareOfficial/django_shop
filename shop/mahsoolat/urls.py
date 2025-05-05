from django.urls import path
from . import views


urlpatterns = [
    path("products" , views.mahsoolatt),
    path("products/<id>", views.devices)

]
