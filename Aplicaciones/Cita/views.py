from django.shortcuts import render, redirect
from Aplicaciones.Cita.models import Contacto


# Create your views here.


def landingpage(request):
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html")


def contacto(request, codigo=''):
    if codigo and codigo == '1234':
        email = "fakemail@arroba.vip"
        nombre = "nombre_prueba"
        prueba = ('test' for _ in range(4))
        comentario, manera, numero, asunto = prueba

        persona = Contacto.objects.create(email=email, nombre=nombre,
                                          comentario=comentario, manera=manera,
                                          numero=numero, asunto=asunto)

    return render(request, "contact.html")


def create_a_contact(request):
    if request.method == 'POST' and request.POST:

        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        comentario = request.POST.get("comentario")
        manera = request.POST.get("manera")
        numero = request.POST.get("numero")
        asunto = request.POST.get("asunto")

        persona = Contacto.objects.create(email=email, nombre=nombre,
                                          comentario=comentario, manera=manera,
                                          numero=numero, asunto=asunto)

        return render(request, 'contact.html')

    return redirect('contact.html')


# mio
#
# def index(request):
#     cita = Cita.objects.all()
#     return render(request, "index2.txt", context={'cita': cita})
#
#
# def registrarCita(request):
#     nombre_cliente = request.POST["nombre_cliente"]
#     telefono = request.POST["telefono"]
#     correo = request.POST["correo"]
#     tamanio = request.POST["tamanio"]
#     fecha_hora = request.POST["fecha_hora"]
#     descripcion = request.POST["descripcion"]
#
#     cita = Cita.objects.create(nombre_cliente=nombre_cliente,
#                                telefono=telefono, correo=correo,
#                                tamanio=tamanio, fecha_hora=fecha_hora,
#                                descripcion=descripcion)
#     return redirect('/')
#
#
# def eliminarCita(request, id_cita):
#     cita = Cita.objects.get(id_cita=id_cita)
#     cita.delete()
#
#     return redirect('/')
