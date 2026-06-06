from django.urls import path
from . import views

urlpatterns = [
    path('tag/<str:slug>/', views.tag_page), # 태그 페이지 URL 연결[cite: 3]
    path('category/<str:slug>/', views.category_page), # 카테고리 페이지 URL 연결[cite: 2]
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]an