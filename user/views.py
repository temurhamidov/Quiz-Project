from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic import CreateView, UpdateView
from django.views import View
from .forms import SignUpForm, ProfileUpdateForm
from django.urls import reverse_lazy

from .models import User


# Create your views here.

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('user:login_view')
    template_name = 'user/signup.html'


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        context = {
            'user' : user
        }
        return render(request, 'user/profile.html', context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    form_class = ProfileUpdateForm
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy('user:profile_view')

class PasswordChangeView(View):
    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
            'messages': 'Xatolik bor'
        }
        return render(request, 'user/change_password.html', context)

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user:profile_view')
        context = {
            'form': form,
            'messages' : 'Xatolik bor'
        }
        return render(request, 'user/change_password.html', context)
