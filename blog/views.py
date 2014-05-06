from django.shortcuts import render_to_response
from blog.models import Post
from django.core import paginator as pgtr

def list_posts(request, page=1):
  post_list = Post.objects.all()
  per_page = 2
  paginator = pgtr.Paginator(post_list, per_page)

  try:
    posts = paginator.page(page)
  except pgtr.PageNotAnInteger:
    # If page is not an integer, deliver first page.
    posts = paginator.page(1)
  except pgtr.EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    posts = paginator.page(paginator.num_pages)

  context = {'posts': posts}
  return render_to_response('blog/post_list.html', context)

def view_post(request):
  pass
