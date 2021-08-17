from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, UserEditForm

# Create your views here.
def index(request):
    return render(request, "auth_app/index.html")

def login(request):
    title = 'вход'
    login_form = UserLoginForm(data=request.POST)
    content = {
        'title': title,
        'login_form': login_form
        }

    if request.method == 'POST' and (login_form.is_valid()):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect(reverse("main_app:index"))

    return render(request, 'auth_app/index.html', content)


def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('main_app:index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()

            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'auth_app/reg.html', content)

def edit(request):
    title = 'редактирование'
    
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
    
    content = {'title': title, 'edit_form': edit_form}
    
    return render(request, 'auth_app/edit.html', content)
