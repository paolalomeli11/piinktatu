from django.db import models
# Create your models here.


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False)
    numero = models.CharField(max_length=10, blank=False, null=True)
    asunto = models.TextField(max_length=250, blank=False, null=True)
    comentario = models.TextField(max_length=250, blank=False)
    manera = models.TextField(max_length=250, null=True)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, null=False)
    usuario = models.CharField(max_length=20, null=False, unique=True)
    contrasenia = models.CharField(max_length=15, null=False, unique=True)

# tamanio_tattoos = [
#     (1, 'Chico (0-10 cm)'),
#     (2, 'Mediano (10-40 cm'),
#     (3, 'Grande (40+ cm')
# ]
#
#
# class Cita(models.Model):
#     id_cita = models.AutoField(primary_key=True)
#     nombre_cliente = models.CharField(max_length=100, null=False)
#     telefono = models.CharField(max_length=10, null=False)
#     correo = models.EmailField(null=False)
#     tamanio = models.IntegerField(choices=tamanio_tattoos, null=False, blank=False)
#     fecha_hora = models.DateTimeField(auto_now=True, null=False)
#     descripcion = models.TextField(max_length=250)
#
#     def __str__(self):
#         return "Id de cita: {0} a nombre de {1} ".format(self.id_cita, self.nombre_cliente)


