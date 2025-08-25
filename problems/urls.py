from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('', views.problem_list, name='problem_list'),  # 문제 목록
    path('<int:pk>/', views.problem_detail, name='problem_detail'),  # 문제 상세
]