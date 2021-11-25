<center>

# Allauth

![Backend](https://camo.githubusercontent.com/04b1c41f01271abc63bc66dc98f7e4eb4f9a4d4036b9d00908ce40a472397534/68747470733a2f2f6366652d7374617469632e73332e616d617a6f6e6177732e636f6d2f6d656469612f616c6c617574682f696d616765732f616c6c5f617574682e706e67)

</center>

Django-allauth es un paquete de instalación de Django de terceros, sirve para administrar el inicio de sesión y el registro de usuarios. Este integra un sistema de usuario local y un sistema de usuario social en donde se pueden asociar multiples cuentas a una sola.

Para mas información sobre el uso de django allauth no hay nada mejor que la documentación oficial. Puedes verla haciendo [***click aquí***](https://django-allauth.readthedocs.io/en/latest/overview.html)


En esta aplicación se utilizó como base las vistas que provee django-allauth después de su intalación para al manejo de sesiones, se realizaron modificaciones a las mismas, asi mismo se agregaron nuevas vistas para el desarrollo de los ejercicios. Se intregó además de la autenticación local la autenticación con [Facebook](https://django-allauth.readthedocs.io/en/latest/providers.html#facebook), [Google](https://django-allauth.readthedocs.io/en/latest/providers.html#google) y [Github](https://django-allauth.readthedocs.io/en/latest/providers.html#github). Para realizar esto se siguieron los pasos de la documentación oficial, enlace que fue definido anteriormente.

## Settings.py

Configuración archivo ``settings.py`` para los proveedores de Facebook, Google y Github



    INSTALLED_APPS = [
        ...
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        # ... Se incluyen los proveedores que definidos para el proyecto
        'allauth.socialaccount.providers.facebook',
        'allauth.socialaccount.providers.google',
        'allauth.socialaccount.providers.github',
        ...
    ]

    # SITE_ID

    SITE_ID = 3

    # Configuración de los proveedores

    SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS': {
                'access_type': 'online',
            }
        },
        'facebook': {
            'METHOD': 'oauth2',
            'SCOPE': ['email', 'public_profile'],
            'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
            'LOCALE_FUNC': lambda request: 'es_CO',
        },
        'github': {
            'SCOPE': [
                'user',
                'repo',
                'read:org',
            ],
        }
    }

    # Configuración proveída por allauth

    ACCOUNT_EMAIL_VERIFICATION = 'optional'
    ACCOUNT_USERNAME_REQUIRED = True
    ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
    ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
    ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
    ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
    ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
    ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
    ACCOUNT_LOGOUT_ON_GET = True



Como fue mencionado anteriormente, para realizar esta configuración en el archivo ``settings.py`` se siguieron los pasos de la documentación oficial, cuyo enlace fue proveído previamente.
