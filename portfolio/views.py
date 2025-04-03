from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import requests
from django.core.paginator import Paginator

# Create your views here.
class PortfolioView(LoginRequiredMixin, ListView):
    model = models.Portfolio
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'portfolio_detail'


class PortfolioDetail(LoginRequiredMixin, DetailView):
    model = models.Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'port_det'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ініціалізуємо repos як None за замовчуванням
        repos = None
        
        # Перевіряємо, чи є github заповненим
        if self.object.github:  # Якщо github не None і не порожній
            github_username = self.object.github.split('/')[-1]  # Отримуємо ім'я користувача з URL
            url = f'https://api.github.com/users/{github_username}/repos'
            response = requests.get(url)
            
            if response.status_code == 200:
                repos_data = response.json()  # Отримуємо список репозиторіїв
                
                # Налаштування пагінації (6 репозиторіїв на сторінку для сітки 3x2)
                paginator = Paginator(repos_data, 6)
                page_number = self.request.GET.get('page')
                repos = paginator.get_page(page_number)
            # Якщо запит до GitHub не вдався, repos залишиться None
            
        context['repos'] = repos  # Додаємо репозиторії (або None) до контексту
        return context
    
class PortfolioCreateView(CreateView):
    model = models.Portfolio
    form_class = forms.PortfolioForm
    template_name = "portfolio/portfolio_create.html"
    success_url = reverse_lazy("users:account")

    def form_valid(self, form):
        # if models.Portfolio.objects.filter(user=self.request.user).exists():
        #     portfolio = models.Portfolio.objects.get(user=self.request.user)
        #     return redirect('portfolio:portfolio_edit', pk=portfolio.pk)

        form.instance.user = self.request.user
        return super().form_valid(form)

    

class PortfolioUpdateView(UpdateView):
    model = models.Portfolio
    form_class = forms.PortfolioForm
    template_name = "portfolio/portfolio_edit.html"
    success_url = reverse_lazy("users:account")

    def get_queryset(self):
        return models.Portfolio.objects.filter(user=self.request.user)