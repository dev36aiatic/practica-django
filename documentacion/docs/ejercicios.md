<center>

# Información y descripción sobre los ejercicios

</center>

![Web Programming](https://www.codeimmersives.com/wp-content/uploads/2021/04/term1.png)

## Restricciones

Para el desarrollo de los 3 ejercicios propuestos durante la practica se hizo uso de rutas hijas y class based views como por ejemplo:

* **TemplateView**: el uso principal es para mostrar información estática como por ejemplo de una colección.
* **CreateView**: el uso principal es para añadir nuevas instancias de un modelo a colección.
* **DeleteView**: el uso principal es para borrar una instancias de un modelo a colección.
* **DetailView**: el uso principal es para mostrar información sobre un objeto específico de una colección.
* **ListView**: el uso principal es para mostrar información sobre una colección específica.
* **UpdateView**: el uso principal es para mostrar actualizar información de un objeto específico de una colección.

Para la creación de la API REST se utilizó [Django REST framework](https://www.django-rest-framework.org/api-guide/generic-views/) y sus vistas genéricas

* **ListAPIView**: sirve para devolver información dada una ruta y un modelo.
* **ListCreateAPIView**: sirve para devolver información y crear una nueva instancia dada una ruta y un modelo junto a sus datos 
* **CreateAPIView**: sirve para crear una nueva instrancia dada una ruta y un modelo junto a sus datos, la diferencia con ListCreateAPIView es que CreateAPIView no devuelve la lista completa cuando se crea un nuevo modelo
* **RetrieveAPIView**: sirve para obtener información sobre un objeto de una colección específica
* **DestroyAPIView**: sirve para borrar un objeto de una colección específica

Para la base de datos se estableció que debía ser PostgreSQL, a continuación se muestra la configuración pertinente en el archivo ``settings.py``

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'xxxxxxxxxxxxxxxxx',
            'USER': 'xxxxxxxxxxxxxxxxx',
            'PASSWORD': 'xxxxxxxxxxxxxxxxx',
            'HOST': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'PORT': '5432',
        },
        'dev': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

``'default'`` es la que utilizará el proyecto por defecto.

Para obtener el token de acceso se utilizó la siguiente funcionalidad que incluye ``rest_framework``

```Python
    from rest_framework.authtoken.views import obtain_auth_token
```

Dado una petición `POST` donde se envía un `username` y `password` devuelve un token de acceso como se observa a continuación: 

![token](../img/token.png)

## Información sobre ejercicio 1

Este ejercicio consistia en permitir que la aplicación permitiera al usuario  iniciar sesión con una cuenta local o una cuenta de redes sociales, asi como registrarse subiendo una foto de perfil tambien que permita a cualquier persona gestionar un tablero en donde se pueden agregar múltiples ideas (notas) las cuales pueden ser públicas o privadas.

Adicionalmente se necesitaban los siguientes endpoints utilizando Django REST framework

| Método http | Endpoint     | Descripción                                                                                    |
|-------------|--------------|------------------------------------------------------------------------------------------------|
| Post        | /token       | Método que permite obtener un token de autenticación mediante username y password.             |
| Get         | /users       | Método que retorna el listado de todos los usuarios con sus diferentes atributos.              |
| Get         | /boards      | Método que retorna todos los tableros creados, permitir filtrar por estrado (privado, público) |
| Post        | /boards      | Método que permite crear un tablero por nombre y estado.                                       |
| Get         | /ideas       | Método que retorna todos las ideas creadas por usuario                                         |
| Post        | /create_idea | Método que permite crear una idea por nombre y estado.                                         |

Para las funcionalidades de iniciar sesión de forma local o con redes sociales se utilizó Django allauth, no se implementó cambios en el código que proveé este mismo, por lo que los únicos cambios que se realizaron fueron de diseño utilizando Bootstrap.

Para ver todo lo relacionado al desarrollo del ejercicio 1 (modelos, formularios, vistas, etc.) para administrar los tableros e ideas ir a [***Desarrollo ejercicio 1***](ejercicio-1.md)

## Información sobre ejercicio 2

Este ejercicio consistia en añadirle a lo desarrollado en el ejercicio 1 las siguientes funcionalidades

* Crear un formulario de contacto
* Responder los comentarios enviados a través del formulario de contacto
* Listar todos los registros del formulario
* Filtrar los registros
* Editar o modificar los registros

Para ver todo lo relacionado al desarrollo del ejercicio 2 ir a [***Desarrollo ejercicio 2***](ejercicio-2.md)

## Información sobre ejercicio 3

Este ejercicio consistia en añadirle a lo desarrollado en el ejercicio 2 los siguientes endpoints

| Método http | Endpoint | Descripción                                                                                                            |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------|
| Post        | /token   | Método que permite obtener un token de autenticación mediante username y password.                                     |
| Post        | /create  | Método que permite crear usuarios almacenando nombre, apellido, número de identificación y foto, el ID debe ser único. |
| Get         | /list    | Método que retorna el listado de todos los usuarios con sus diferentes atributos.                                      |
| Get         | /user    | Método que recibe el ID de usuario y retorna el usuario con sus atributos. (detail)                                    |
| Delete      | /delete  | Método que reciba en la url un identificador y elimine el usuario que tenga ese identificador.                         |



Para ver todo lo relacionado al desarrollo del ejercicio 3 ir a [***Desarrollo ejercicio 3***](ejercicio-3.md)


