from django.urls import path
from evaluacion import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('productos', views.productos, name = 'productos'),
    path('contacto', views.contacto, name = 'contacto'),
    path('inventario', views.inventario, name = 'inventario'),
    path('admin', views.admin, name = 'admin'),
]