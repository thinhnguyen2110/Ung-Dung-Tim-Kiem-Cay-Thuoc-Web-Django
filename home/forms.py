from django import forms
from .models import *


class FormDangKi(forms.Form):
    username = forms.CharField(label='Họ và Tên',max_length=200)
    email = forms.EmailField()
    password = forms.CharField(label='Mật Khẩu',max_length=20, widget=forms.PasswordInput)


class FormDangNhap(forms.Form):
    username = forms.CharField(label='Họ và Tên',max_length=200)
    password = forms.CharField(label='Mật Khẩu',max_length=20, widget=forms.PasswordInput)



