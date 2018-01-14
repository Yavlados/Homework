from django import forms
from django.core.exceptions import ValidationError
from my_app.models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите пароль')
    email = forms.EmailField(widget=forms.EmailInput, label='E-mail')
    firstname = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password != password2:
            raise ValidationError("Пароли должны совпадать")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise ValidationError("Пользователь с таким именем уже существует")
        return username


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["name_shop", "adr_shop"]
        widgets = {'name_shop': forms.Textarea(attrs={'resize': 'none'})}


class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ['name_tovar', 'type_tovar', 'photo_tovar', 'opisanie_tovar']
        widgets = {'name_tovar': forms.Textarea(attrs={'resize': 'none'})}


class FbForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['']

class Tovar_add_Form(forms.ModelForm):
    class Meta:
        model = Tovar
        exclude = ['']