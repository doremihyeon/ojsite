from django.http import HttpResponse
from django.shortcuts import render

def contest_list(request):
    return HttpResponse("대회 목록 페이지입니다.")

def contest_detail(request, pk):
    return HttpResponse(f"대회 상세 페이지입니다. (id={pk})")
