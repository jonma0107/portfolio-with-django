from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    pass
