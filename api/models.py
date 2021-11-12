import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from practicas import settings

def img_uploader(instance, filename):
    image_name = 'user_images/{0}/profile.jpg'.format(instance.username)
    full_path = os.path.join(settings.MEDIA_ROOT, image_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return image_name

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, first_name, last_name, id_num, password, **extra_fields):
        if not email:
            raise ValueError('Correo electrónico obligatorio.')
        if not username:
            raise ValueError('Nombre de usuario obligatorio')
        if not first_name:
            raise ValueError('Los nombres son obligatorios')
        if not last_name:
            raise ValueError('Apellidos son obligatorios')
        if not id_num:
            raise ValueError('Número de identificación obligatorio')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            id_num=id_num,
            last_login=timezone.now(),
            date_joined=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, first_name, last_name, id_num, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, username, first_name, last_name, id_num, password, **extra_fields)

    def create_superuser(self, email, username, first_name, last_name, id_num, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuario debe ser personal.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Super usuario debe ser administrador.')

        return self._create_user(email, username, first_name, last_name, id_num, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255, verbose_name='Correo electrónico', unique=True)
    username = models.CharField(
        max_length=28, verbose_name='Usuario', unique=True, default='')
    first_name = models.CharField(max_length=80, verbose_name='Nombres', default='')
    last_name = models.CharField(max_length=80, verbose_name='Apellidos', default='')
    id_num = models.CharField(
        max_length=12, verbose_name='Número de identificación', unique=True)
    date_joined = models.DateTimeField(
        verbose_name="Creado en", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="Último inicio de sesión", auto_now=True)
    profile_picture = models.ImageField(verbose_name="Foto", default="user.png", upload_to=img_uploader, blank=True)

    is_active = models.BooleanField(verbose_name="Activo", default=True)
    is_admin = models.BooleanField(
        verbose_name="Administrador", default=False)  # a superuser
    # a admin user; non super-user
    is_staff = models.BooleanField(verbose_name="Personal", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'id_num', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    @staticmethod
    def has_perm(self, *args, **kwargs):
        return True

    @staticmethod
    def has_module_perms(self, *args, **kwargs):
        return True


class Board(models.Model):

    PUBLIC = 'PU'
    PRIVATE = 'PR'
    BOARD_STATUS = [
        (PUBLIC, 'Publico'),
        (PRIVATE, 'Privado')
    ]
    name = models.CharField(max_length=36)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=2, choices=BOARD_STATUS, default=PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.id } - { self.name } | { self.owner }"


class Ideas(models.Model):
    PUBLIC = 'PU'
    PRIVATE = 'PR'
    BOARD_STATUS = [
        (PUBLIC, 'Publico'),
        (PRIVATE, 'Privado')
    ]
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=36)
    status = models.CharField(
        max_length=2, choices=BOARD_STATUS, default=PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.id } - { self.name } | { self.owner }"
