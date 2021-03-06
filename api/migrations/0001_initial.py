# Generated by Django 3.2.9 on 2021-11-12 16:53

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electrónico')),
                ('username', models.CharField(default='', max_length=28, unique=True, verbose_name='Usuario')),
                ('first_name', models.CharField(default='', max_length=80, verbose_name='Nombres')),
                ('last_name', models.CharField(default='', max_length=80, verbose_name='Apellidos')),
                ('id_num', models.CharField(max_length=12, unique=True, verbose_name='Número de identificación')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Último inicio de sesión')),
                ('profile_picture', models.ImageField(blank=True, default='user.png', upload_to=api.models.img_uploader, verbose_name='Foto')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Administrador')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Personal')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('status', models.CharField(choices=[('PU', 'Publico'), ('PR', 'Privado')], default='PU', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ideas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('status', models.CharField(choices=[('PU', 'Publico'), ('PR', 'Privado')], default='PU', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.board')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
