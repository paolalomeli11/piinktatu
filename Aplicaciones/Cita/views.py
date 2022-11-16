from django.shortcuts import render, redirect
from Aplicaciones.Cita.models import Contacto, Usuario


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


def login_registro(request):
    if request.method == 'POST' and request.POST:
        usuario = Usuario.objects.create(usuario=request.POST.get("usuario"),
                                         contrasenia=request.POST.get("contrasenia"))

    return render(request, 'registro_login.html')


def usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, "usuarios.html", context={'usuarios': usuario})


def eliminarUsuario(request, id_usuario):
    Usuario.objects.get(id_usuario=id_usuario).delete()
    return redirect('usuarios')


def edit_page(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    return render(request, 'editar.html', {'usuario': usuario})


def editUser(request, id_usuario):
    if request.method == 'POST' and request.POST:
        usuario = request.POST['usuario']
        contrasenia = request.POST['contrasenia']

        user = Usuario.objects.get(id_usuario=id_usuario)

        user.usuario = usuario
        user.contrasenia = contrasenia

        user.save()

        return redirect('usuarios')

    return redirect('usuarios')


def login(request):
    return render(request, 'login.html')


def acceder(request):
    if request.method == 'POST' and request.POST:
        usuario = request.POST.get('usuario')
        contrasenia = request.POST.get('contrasenia')

        usuario_db = Usuario.objects.get(usuario=usuario, contrasenia=contrasenia)

        if usuario_db.usuario == usuario and usuario_db.contrasenia == contrasenia:
            return render(request, 'usuarios.html', context={'usuarios': Usuario.objects.all()})

    return redirect('login')


def agregarUsuario_page(request):
    return render(request, 'agregar.html')


def agregarUsuario(request):
    if request.method == 'POST' and request.POST:
        usuario = request.POST.get("usuario")
        contrasenia = request.POST.get("contrasenia")

        usuario_clase = Usuario.objects.create(usuario=usuario, contrasenia=contrasenia)
        context = Usuario.objects.all()

        return render(request, 'usuarios.html', {'usuarios': context})

    return redirect('usuarios.html')
