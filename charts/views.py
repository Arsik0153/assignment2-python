from django.shortcuts import render
from .models import AccountInfo

def index(request):
    accountinfos = AccountInfo.objects.all()

    context = {
        "accountinfos" : accountinfos
    }

    return render(request, 'chart_page/index.html', context)
