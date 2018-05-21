from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post,Category,Tag
import markdown
import pygments
from comments.forms import CommentForm

def index(request):
    # return HttpResponse('welcome my blog')
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list':post_list})




def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'detail.html', context=context)

    # return render(request, 'detail.html', {'post':post})



def archives(request, year, month, day):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    created_time__day =day,

                                    ).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})
