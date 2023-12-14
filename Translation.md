# Pasos Traducción - Internacionalización de Django

## Paso No. 1: Configurar el archivo de settings.py

1. Activa el middleware local en la configuración de Django.
   
   ```python
   MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
   ]
   ```
2. Especifica las cadenas de traducción en las plantillas.

    ```python
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
    ]
    ```
3. Implementa las traducciones para esas cadenas, en cualquiera de los lenguajes que quieras soportar.

   ```python
   # Internationalization
   # https://docs.djangoproject.com/en/4.2/topics/i18n/
  
   LANGUAGE_CODE = 'en'
  
   TIME_ZONE = 'America/Bogota'
  
   USE_I18N = True
  
   USE_L10N = True
  
   USE_TZ = True
  
   from django.utils.translation import gettext_lazy as _
  
   LANGUAGES = [
      ('es', _('Spanish')),
      ('en', _('English')),
      ('ja', _('Japanese')),
      ('fr', _('French')),
      ('de', _('German')),
      ('ru', _('Russian')),
   ]
  
   LOCALE_PATHS = [
      os.path.join(BASE_DIR, 'locale')
   ]
   ```

## Paso No. 2 : Marcar texto a traducir

* Texto en plantillas: 
  Lo primero es cargar la etiqueta {% load i18n %} en el template de django, para una línea sencilla utilizamos el templatetag {% trans 'texto' %}
  pero si tenemos contenido un poco más complejo, por ejemplo que incluya multiples elementos HTML o variables,
  utilizaremos los templatetag blocktrans / endblocktrans.

  ```python
  {% extends 'layout.html' %}

  {% block content %}

  {% load static %}

  {% load i18n %}

  <header class="row">

    <div class="col-md-4 d-flex align-items-center justify-content-center">
      <img class="profile rounded mb-4 border border-info border-3 shadow-lg" src="{% static 'files/perfil2.webp' %}" alt="profile">
    </div>
  
    <div class="col-md-8 m-auto">
      <h1> {% trans "I am" %} <strong>Jonathan Meza</strong></h1>
      <h3>Python FullStack Developer</h3>
      <p>
        {% blocktrans trimmed %}
        Full-stack developer specialized in Python with a strong background in software engineering and proven experience in the design,
        development and implementation of complete and efficient web applications. My versatile approach has allowed me to contribute
        to both client-side and server-side development, providing comprehensive and functional solutions.
        {% endblocktrans %}      
      </p>    
    </div>  
  </header>
  ```
## Paso No. 3.

 * El siguiente paso es para crear las urls globales en el archivo urls.py del directorio del proyecto

 ```python
  from django.contrib import admin
  from django.conf.urls.i18n import i18n_patterns
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [   
      path('i18n/', include('django.conf.urls.i18n')), 
  ]
  
  
  urlpatterns += i18n_patterns(
      path('admin/', admin.site.urls), 
      path('', include('app_portfolio.urls')),
      path('blog/', include('app_blog.urls')), 
  ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 ```
## Paso No. 4: Crear archivos de traducción

Ya tenemos todo configurado, ahora vamos a crear los archivos de traducción con el siguiente comando:

`django-admin makemessages -l en_US`

Se crearán en la ruta:

`some_project\locale\en_US\LC_MESSAGES\django.po`

```
#. Translators: Este mensaje aparece en la página de inicio únicamente.
# path/to/python/file.py:123
msgid "Bienvenidos a mi sitio."
msgstr ""
```

Estos archivos son los que utilizaremos para especificarle a Django cómo traducir cada palabra en determinado idioma, entonces simplemente para cada uno de los strings que aparezcan en `msgid` podemos especificar su traducción con los strings msgstr:

```
msgid "Bienvenidos a mi sitio."
msgstr "Welcome to my site."
```

### Compilar archivos de traducción

Una vez tengamos nuestros archivos de traducción completos, procederemos a compilarlos con el siguiente comando:

`django-admin compilemessages`

Cuando compilemos nuestros archivos, ya podemos utilizar nuestro proyecto en el idioma especificado. Cada que uno de nuestros usuarios consulte nuestro proyecto aparecerá en su idioma. Para efectos de prueba, podemos cambiar el lenguaje del proyecto por inglés y observar los resultados:

`LANGUAGE_CODE = 'en-us'`

### Ejemplo de salida de comandos

```bash
(my_env) C:\Users\agency_project>django-admin makemessages -l en_US
processing locale en_US

(my_env) C:\Users\agency_project>django-admin compilemessages
processing file django.po in C:\Users\agency_project\locale\en_US\LC_MESSAGES
```
## NOTAS:

* Intentando internacionalizar una aplicación Django el problema es cuando se intenta ejecutar el comando para crear archivos de idioma:
```bash
python manage.py makemessages -l fr
It outputs an error :

CommandError: Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed.
```
## Solución:

* Primero cree un directorio en la carpeta raíz del proyecto con el nombre localey luego ejecute

```bash
sudo apt install gettext
```
* Verifique o agregue en settings.py :
  
`LOCALE_PATHS = (BASE_DIR + 'locale/', )`

* Y en la terminal digitar:     

```bash
pip install djangorestframework-jwt --upgrade
```  
