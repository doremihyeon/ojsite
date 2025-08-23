from django.urls import path
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),  # 과제 목록
    path('<int:pk>/', views.assignment_detail, name='assignment_detail'),  # 특정 과제 상세
]