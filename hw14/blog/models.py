from django.db import models
from django.contrib.auth.models import User

# 1. 카테고리 모델 (다대일)[cite: 2]
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) # 고유한 이름[cite: 2]
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # 한글 URL 지원[cite: 2]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/' # 카테고리 고유 URL[cite: 2]

    class Meta:
        verbose_name_plural = 'Categories' # 복수형 이름 지정[cite: 2]

# 2. 태그 모델 (다대다)[cite: 3]
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/' # 태그 고유 URL[cite: 3]

# 3. 포스트 모델에 연결!
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # 작성자 연결[cite: 2]
    
    # 카테고리 연결 (다대일) - 삭제 시 빈칸(null) 처리[cite: 2]
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    # 태그 연결 (다대다) - 다대다 필드는 기본적으로 null=True 설정이 되어 있습니다[cite: 3].
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'