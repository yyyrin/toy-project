from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'), # 전체 영화 목록 페이지 조회
    path('new/', views.new, name='new'),  # 새로운 영화 생성 페이지 조회
    path('create/', views.create, name='create'),  # 단일 영화 데이터 저장
    path('<movie_id>/', views.detail, name='detail'),  # 단일 영화 상세 페이지 조회 
    path('<movie_id>/edit/', views.edit, name='edit'),  # 기존 영화 수정 페이지 조회
    path('<movie_id>/update/', views.update, name='update'),  # 단일 영화 데이터 수정
    path('<movie_id>/delete/', views.delete, name='delete'),  # 단일 영화 데이터 삭제
]
