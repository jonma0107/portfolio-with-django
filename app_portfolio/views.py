from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
  """
  CONSULTAR A BASE DE DATOS
  """
  projects = Project.objects.all()
  return render(request, 'home.html', {'projects':projects})