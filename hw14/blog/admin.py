from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)

# name 필드 값 입력 시 slug 자동 생성[cite: 2]
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} # 태그도 slug 자동 채움[cite: 3]
