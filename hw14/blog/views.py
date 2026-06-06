from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class PostList(ListView):
    model = Post
    ordering = '-pk'

    # 템플릿에 카테고리 목록과 미분류 개수를 함께 넘겨줌[cite: 2]
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    # 상세 페이지에도 카테고리 목록 넘겨줌[cite: 2]
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 카테고리 필터링 함수 (FBV)[cite: 2]
def category_page(request, slug):
    if slug == 'no_category': # 미분류 카테고리 처리[cite: 2]
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category,
    })

# 태그 필터링 함수 (FBV)[cite: 3]
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug) # URL 인자와 동일한 slug를 가진 태그 불러오기[cite: 3]
    post_list = tag.post_set.all() # 태그에 연결된 포스트 전체 저장[cite: 3]

    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'tag': tag,
    })