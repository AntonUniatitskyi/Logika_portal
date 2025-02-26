from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import UserForm, EmailPasswordForm
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
import core.settings
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
    success_url = reverse_lazy('users:account')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Ваш профіль успішно оновлено")
        return response

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

                subject = user.username
                message = f'Вітаємо, {subject}. Ви успішно зареєстровані! Ми раді вас бачити'
                from_email = core.settings.EMAIL_HOST_USER
                to_email = user.email
                send_mail(
                    subject,
                    message,
                    from_email, 
                    [to_email],
                    fail_silently=False
                )

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
                    subject = admin.username
                    message = f'Вітаємо, {subject}. Ви успішно увійшли в свій акаунт! Ми раді вас бачити'
                    from_email = core.settings.EMAIL_HOST_USER
                    to_email = admin.email
                    send_mail(
                        subject,
                        message,
                        from_email, 
                        [to_email],
                        fail_silently=False
                    )
                    return redirect('home')
                else:
                    messages.error(request, 'Невірний пароль!')
                    return redirect('users:login')
            except User.DoesNotExist:
                messages.error(request, 'Користувач або адмін з таким email не знайдено.')
                return redirect('users:login')

    else:
        form = EmailPasswordForm()
    return render(request, 'users/request_login.html', {'form': form})