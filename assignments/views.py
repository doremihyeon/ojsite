from django.http import HttpResponse
from django.shortcuts import render

def assignment_list(request):
    return HttpResponse("과제 목록 페이지입니다.")

def assignment_detail(request, pk):
    return HttpResponse(f"과제 상세 페이지입니다. (id={pk})")