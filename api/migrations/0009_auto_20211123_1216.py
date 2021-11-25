# Generated by Django 3.2.9 on 2021-11-23 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_replymessage_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.board', verbose_name='Tablero'),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='name',
            field=models.CharField(max_length=36, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador'),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='status',
            field=models.CharField(choices=[('PU', 'Publico'), ('PR', 'Privado')], default='PU', max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='replymessage',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.contact', verbose_name='Contacto'),
        ),
        migrations.AlterField(
            model_name='replymessage',
            name='reply',
            field=models.TextField(verbose_name='Escribir respuesta'),
        ),
    ]