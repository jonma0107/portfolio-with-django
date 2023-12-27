from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post(request):
  """
  Consultar a la base de datos
  """
  posts= Post.objects.all()
  blog_clicked = request.GET.get('blog_clicked', False)
  return render(request, 'posts.html', {'posts':posts, 'blog_clicked': blog_clicked})

def post_detail(request, post_id):
  """
  Consultar a la base de datos el id si existe o no,
  para retornar una publicación
  """
  post=get_object_or_404(Post, pk=post_id)
  blog_clicked = request.GET.get('blog_clicked', False)
  return render(request, 'post_detail.html', {'post':post, 'blog_clicked': blog_clicked})

