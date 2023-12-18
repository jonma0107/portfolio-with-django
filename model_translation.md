# Pasos para tradución de modelos

Para internacionalizar los modelos haremos uso de la libreria [`Django Parler`](https://django-parler.readthedocs.io/)

## Paso 1: Instalar en entorno virtual:

```bash
pip install django-parler
```
## Paso 2: Configuración en settings

Edita el archivo `settings.py` y adiciona `parler` a las aplicaciones instaladas:

```python
INSTALLED_APPS = [
    ...
    'parler',
    ...
]
```

Luego continua con las configuraciones de Django Parler:

```python
PARLER_LANGUAGES = {
    None: (
        {'code': 'es', },
        {'code': 'en', },
        {'code': 'ja', },
        {'code': 'fr', },
        {'code': 'de', },
        {'code': 'ru', },
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

PARLER_DEFAULT_LANGUAGE_CODE = 'en'
PARLER_SHOW_EXCLUDED_LANGUAGE_TABS = True
```
## Paso 3: Modificación de modelos para traducciones

`Django-parler` ofrece la clase `TranslatedModel` para los modelos y el _wrapper_ `TranslatedFields` para envolver los campos de los modelos que se quieren traducir.

```python
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Post(TranslatableModel):
  translations = TranslatedFields(
        title = models.CharField(max_length=150, verbose_name=_("titulo"), null=True),
        content = models.TextField(verbose_name=_("contenido"))
    ) 
  
  image = models.ImageField(upload_to='blog/images/')
  date = models.DateField(datetime.date.today)

  def __unicode__(self):
        return self.title
```
## Paso 4: Integrando traducciones en el sitio de administración

`Django-parler` administra las traducciones y genera una tabla adicional por cada modelo a traducir, llamada _app_model_translation_. En la intefaz de administración crea una nueva pestaña (tab) para cada idioma a usarse, para ello es necesario hacer que los modelos hereden de `TranslatableAdmin`:

```python
# admin.py

from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    pass
```
## Paso 5: Creando migraciones para los modelos de traducciones:

```bash
python manage.py makemigrations
python manage.py migrate
```
