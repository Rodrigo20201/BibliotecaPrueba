from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('logout/', views.logout_usuario, name='logout'),
    path('inicio_lector/', views.inicio_lector, name='inicio_lector'),
    path('dashboard_bibliotecario/', views.dashboard_bibliotecario, name='dashboard_bibliotecario'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin')
]
