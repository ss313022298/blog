from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['-created_time']







