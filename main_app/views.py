from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Scp, Profile, Canon, Tales
from .forms import Scp_Form, Edit_Scp_Form, Tale_Form, Edit_Tale_Form, QuillFormField, RegisterForm
# Create your views here.
def home(request):
    tales_list = Tales.objects.all()
    context = {'tales_list' : tales_list}
    return render(request, 'home.html', context)
def minor_index(request):
    scp_list = Scp.objects.all().order_by('number')
    context = {'scp_list' : scp_list}
    return render(request, 'minor/index.html', context)
def minor_events(request):
    return render(request, 'minor/events.html')
def minor_locations(request):
    return render(request, 'minor/locations.html')
def minor_items(request):
    return render(request, 'minor/items.html')
def minor_items1(request):
    return render(request, 'minor/items1.html')
def minor_items2(request):
    return render(request, 'minor/items2.html')
def staff_self(request):
    current_user = request.user
    if request.user.is_authenticated:
        myscp_list = Scp.objects.filter(author = current_user)
        mytale_list = Tales.objects.filter(author = current_user)
        print(mytale_list)
        context = {
            'user': current_user,
            'scp_list': myscp_list,
            'tale_list': mytale_list,
        }
        return render(request, 'staff/show.html', context)
    else:
        return redirect('staff/new')
def profile_redirect(request):
    return redirect('/staff/self')
def about(request):
    return render(request, 'about.html')
def gois(request):
    return render(request, 'gois/index.html')
def internal(request):
    return render(request, 'internal/index.html')
def staff_new(request):
    error_message=''
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            article = Profile
            article = form.save(commit=False)
            article.save()
            return redirect('home')
        else:
            print(form.errors)
            error_message = form.errors
    form = RegisterForm()
    context = {'form' : form }
    return render(request, 'staff/new.html', context)
def scp_show(request, scp_number):
    scp = Scp.objects.get(id=scp_number)
    if request.user == scp.author:
        return redirect('/scp/edit/{}'.format(scp_number))
    else:
        print(scp.body)
        context = { 'scp' : scp }
        print(context)
        return render(request, 'articles/show.html', context)
def tale_show(request, tale_id):
    tale = Tales.objects.get(id=tale_id)
    print(tale.title)
    context = {'tale' : tale}
    return render(request, 'tales/show.html', context)
def scp_new(request):
    error_message=''
    if request.method == "POST":
        form = Scp_Form(request.POST)
        if form.is_valid():
            author = request.user
            article = Scp
            article = form.save(commit=False)
            article.user = author
            article.save()
            return redirect('home')
        else:
            print(form.errors)
            error_message = form.errors
    # current_user = request.user
    form = Scp_Form()
    context = {'form' : form, 'error_message': error_message}
    return render(request, 'articles/new.html', context)
def scp_edit(request, scp_id):
    error_message=''
    current_scp = Scp.objects.get(id=scp_id)
    if request.method == "POST":
        current_scp = Scp.objects.get(id=scp_id)
        form = Scp_Form(instance=current_scp)
        if form.is_valid():
            article = Scp.objects.get(id=scp_id)
            if request.POST['title']:
                article.title = request.POST['title']
            if request.POST['number']:
                article.number = request.POST['number']
            if request.POST['body']:
                article.body = request.POST['body']
            if request.POST['canon']:
                canon_id = request.POST['canon']
                canon = Canon.objects.get(id=canon_id)
                post.canon = canon
            article.save()
            return redirect('/staff/self')
        else:
            print(form.errors)
            error_message = form.errors
    form = Edit_Scp_Form(initial={'title' : current_scp.title, 'body' : current_scp.body, 'number' : current_scp.number, 'canon' : current_scp.canon})
    context = {'form' :  form, 'scp' : current_scp}
    return render(request, 'articles/edit.html', context)
            

def tale_new(request):
    error_message=''
    if request.method == "POST":
        form = Tale_Form(request.POST)
        if form.is_valid():
            author = 1 #request.user
            article = Tales
            article = form.save(commit=False)
            article.user = author
            article.save()
            return redirect('home')
        else:
            print(form.errors)
            error_message = form.errors
    # current_user = request.user
    form = Tale_Form()
    context = {'form' : form, 'error_message': error_message}
    return render(request, 'tales/new.html', context)
def scp_index(request):
    scp_list = Scp.objects.all().order_by('number')
    context = {'scp_list' : scp_list}
    return render(request, 'articles/index.html', context)