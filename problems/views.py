from django.shortcuts import render
from django.http import HttpResponse

def problem_list(request):
    return HttpResponse("문제 목록 페이지")

def problem_detail(request, pk):
    return HttpResponse(f"문제 상세 페이지: {pk}")