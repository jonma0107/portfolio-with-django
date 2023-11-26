from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog(request):
  """
  Consultar a la base de datos
  """
  blogs= Post.objects.all()
  return render(request, 'posts.html', {'blogs':blogs})

def blog_detail(request, blog_id):
  """
  Consultar a la base de datos el id si existe o no,
  para retornar una publicación
  """
  blog=get_object_or_404(Post, pk=blog_id)
  return render(request, 'post_detail.html', {'blog':blog})

