from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage),
    path('landingpage/', views.landingpage, name='landingpage'),
    path('galeria/', views.gallery, name='gallery'),
    path('contacto/', views.contacto, name='contacto'),
    path('createContact/', views.create_a_contact, name='create_a_contact'),
    path('contacto/<str:codigo>/', views.contacto, name='create_fake_contact'),
    path('login_registro/', views.login_registro, name='login'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('edit_page/<str:id_usuario>', views.edit_page, name='edit_page'),
    path('eliminarUsuarios/<str:id_usuario>', views.eliminarUsuario, name='delete_usuario'),
    path('login/', views.login, name='login_acceso'),
    path('acceder/', views.acceder, name="acceder"),
    path('editarUsuario/<str:id_usuario>', views.editUser, name='editUser'),
    path('agregarUsuario/', views.agregarUsuario_page, name='agregarUser'),
    path('agregarUsuarioRegistro/', views.agregarUsuario, name='agregarUserRegistro')
]
