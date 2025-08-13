from django.shortcuts import HttpResponse

def signup_view(request):
    return HttpResponse("회원가입 페이지입니다.")