from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='parqueadero/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('registrar-vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('listar-vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('registrar_funcionario/', views.registrar_funcionario, name='registrar_funcionario'),
    path('eliminar_funcionario/<int:pk>/', views.eliminar_funcionario, name='eliminar_funcionario'),
    path('editar_funcionario/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),

]
