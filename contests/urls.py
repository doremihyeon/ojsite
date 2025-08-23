from django.urls import path
from . import views

app_name = 'contests'  # 네임스페이스 구분용

urlpatterns = [
    path('', views.contest_list, name='contest_list'),  # 대회 목록
    path('<int:pk>/', views.contest_detail, name='contest_detail'),  # 특정 대회 상세
]