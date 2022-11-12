from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage),
    path('landingpage/', views.landingpage, name='landingpage'),
    path('galeria/', views.gallery, name='gallery'),
    path('contacto/', views.contacto, name='contacto'),
    path('createContact/', views.create_a_contact, name='create_a_contact'),
    path('contacto/<str:codigo>/', views.contacto, name='create_fake_contact')
]
