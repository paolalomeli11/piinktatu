# Generated by Django 4.1.3 on 2022-11-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cita', '0003_contacto_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='manera',
            field=models.TextField(max_length=250, null=True),
        ),
    ]