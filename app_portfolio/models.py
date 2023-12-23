from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Project(TranslatableModel):
  translations = TranslatedFields(
        description = models.CharField(max_length=250, verbose_name=_("descripcion"))
    )
  
  title = models.CharField(max_length=150, verbose_name=_("titulo"))
  
  image = models.ImageField(upload_to='portfolio/images/')
  url = models.URLField(blank=True)
  demo = models.URLField(blank=True)

  def __str__(self):
      return self.title
  

