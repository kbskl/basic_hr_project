from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from account.forms import LoginForm, RegisterForm


def login(request):
    if request.user.is_authenticated:
        if 'next' in request.GET:
            return redirect(request.GET.get('next'))
        return redirect('core:home')
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('core:home')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.POST and 'registerSubmit' in request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('account:login')
    else:
        register_form = RegisterForm()
    context = {
        'register_form': register_form,
    }
    return render(request, 'account/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('account:login')
