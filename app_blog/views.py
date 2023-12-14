from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post(request):
  """
  Consultar a la base de datos
  """
  posts= Post.objects.all()
  return render(request, 'posts.html', {'posts':posts})

def post_detail(request, post_id):
  """
  Consultar a la base de datos el id si existe o no,
  para retornar una publicación
  """
  post=get_object_or_404(Post, pk=post_id)
  return render(request, 'post_detail.html', {'post':post})

