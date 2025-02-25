from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import UserForm, EmailPasswordForm
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProfileAboutView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/account.html'
    context_object_name = 'account_detail'

    def get_object(self):
        return self.request.user

class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update_account.html'
    success_url = reverse_lazy('account')

def logout_view(request):
    logout(request)
    return redirect('home')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                request.session['username'] = user.username
                messages.success(request, 'Користувач успішно створений!')
                return redirect('home')
            except IntegrityError:
                messages.error(request, 'Користувач з такою поштою вже зареєстрований.')
        else:
            print(form.errors)
            messages.error(request, 'Виникла помилка. Перевірте введені дані.')
    else:
        form = UserForm()
    
    return render(request, 'users/create_user.html', {'form': form})


def request_login(request):
    if request.method == 'POST':
        form = EmailPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Перевірка користувача
            try:
                admin = User.objects.get(email=email)
                if admin.check_password(password):
                    login(request, admin)
                    request.session['username'] = admin.username
                    messages.success(request, 'Ви успішно увійшли як адмін!')
                    return redirect('home')
                else:
                    messages.error(request, 'Невірний пароль!')
                    return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Користувач або адмін з таким email не знайдено.')
                return redirect('login')

    else:
        form = EmailPasswordForm()
    return render(request, 'users/request_login.html', {'form': form})