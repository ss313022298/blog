from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


# Create your models here.
# 创建分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 创建标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 创建文章
class Post(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:76]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # 正文
    body = models.TextField()
    # 创建时间
    created_time = models.DateField()
    # 修改时间
    modified_time = models.DateField()
    # 分类和文章,一对多关系
    category = models.ForeignKey(Category)
    # 标签和文章,多对多关系(文章可能没有标签)
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者和文章,一对多关系
    author = models.ForeignKey(User)
    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])








