from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Scp, User, Canon, Tales
# Create your views here.
def home(request):
    return render(request, 'home.html')

def scp_show(request, scp_number):
    scp = Scp.objects.get(number=scp_number)
    print(scp.title)
    context = { 'scp' : scp }
    print(context)
    return render(request, 'articles/show.html', context)