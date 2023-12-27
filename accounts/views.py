from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from nagoyameshi.models import Member

from .forms import SignupForm

# NoReverseMatchエラー 対応
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('nagoyameshi:top')

class CustomLoginView(LoginView):
    next_page = reverse_lazy('nagoyameshi:top')


class SignupView(CreateView):
    model = Member
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('nagoyameshi:top')
    # success_url = reverse_lazy('accounts:login')