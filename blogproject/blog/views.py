from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post,Category,Tag
import markdown
import pygments

def index(request):
    # return HttpResponse('welcome my blog')
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list':post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', {'post':post})
