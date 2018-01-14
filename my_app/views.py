from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from my_app.forms import *
from my_app.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def main(request):
    return render(request, 'main.html', locals())


class TovarList(ListView):
    form_class = TovarForm
    model = Tovar
    template_name = "tovar.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.all()
        return context


def tovar_show(request):
    id = request.GET.get('id')
    if id:
        tovar = Tovar.objects.filter(id_tovar=id)
        fb = Feedback.objects.filter(tovar=id)
        return render(request, "tovar_show.html", locals())
    else:
        return render(request, "tovar.html", {'tovar': Tovar.objects.all()})



class ShopList(ListView):
    form_class = ShopForm
    model = Shop
    template_name = "shop.html"
    paginate_by = 5


def fb_add(request):
    tovar = Tovar.objects.all()
    fb = Feedback.objects.all()
    form = FbForm(request.POST or None, request.FILES or None)
    context = {"form": form, "tovar": tovar, "tutors": fb}
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('tovar_url'))
    return render(request, "feedback_add_form1.html", locals())

def good_add(request):
    tovar = Tovar.objects.all()
    form = Tovar_add_Form(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('tovar_url'))
    return render(request, "good_add_form.html", locals())


def registration(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not errors:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=surname)
            return HttpResponseRedirect(reverse('login_url'))
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main_url'))
        else:
            error = "Пользователь не найден"
    return render(request, 'login.html', locals())


@login_required()
def success(request):
    return render(request, reverse('success_url'), locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main_url'))


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            password=request.POST.get('password'),
                                            email=request.POST.get('email'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname')
                                            )
            return HttpResponseRedirect(reverse('login_url'))
        else:
            print(form.cleaned_data)
    return render(request, 'registration2.html', {'form': form}, locals())
