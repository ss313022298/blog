from ..models import Post,Category,Tag
from django import template

register = template.Library()
#
@register.simple_tag
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.all().dates('created_time', 'day', order='DESC')

# 分类模板标签
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()