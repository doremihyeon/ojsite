from django.shortcuts import render
from .models import Contest

def contest_list(request):
    contests = Contest.objects.all()
    return render(request, 'contests/contest_list.html', {'contests': contests})