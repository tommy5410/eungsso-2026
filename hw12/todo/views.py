# todo/views.py
from django.shortcuts import render
from .models import Post  # 🚨 옛날 TodoItem 대신 Post를 가져옵니다!

# 1. 게시글 목록 페이지 (최신순 정렬) [cite: 447, 448]
def index(request):
    posts = Post.objects.all().order_by('-pk')  # 최신 글이 맨 위로! [cite: 448, 450]
    return render(request, 'todo/post_list.html', {'posts': posts})

# 2. 게시글 상세 페이지 [cite: 453]
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)  # 클릭한 게시글 1개 땡겨오기 [cite: 467]
    return render(request, 'todo/post_detail.html', {'post': post})

# 3. 과제 필수 조건: 기본 랜딩 페이지 [cite: 705, 718]
def landing(request):
    return render(request, 'todo/landing.html')

# 4. 과제 필수 조건: 자기소개 페이지 [cite: 705, 718]
def about_me(request):
    return render(request, 'todo/about_me.html')