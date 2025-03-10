from . import models
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import MaterialForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class MaterialListView(LoginRequiredMixin, ListView):
    model = models.Materials
    template_name = 'materials/materials.html'
    context_object_name = 'materials'
    ordering = '-created_at'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_material'] = self.get_queryset()
        if self.request.user.has_perm('materials.view_event'):
            context['add_material'] = MaterialForm()
        else:
            context['add_material'] = None
        return context
    def post(self, request, *args, **kwargs):
        form = MaterialForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.uploaded_by = self.request.user
            event.save()
            messages.success(request, "Матеріал додано, перегляньте сторінку.")
            return redirect('materials:materials')
        else:
            messages.error(request, "Форма невалідна!")
            return redirect('materials:materials')
        
class MaterialUpdateView(UpdateView):
    model = models.Materials
    form_class = MaterialForm
    template_name = 'materials/materials.html'
    success_url = reverse_lazy('materials:materials')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Матеріал успішно змінено")
        return response

class MaterialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Materials
    template_name = 'materials/delete_material.html'
    success_url = reverse_lazy('materials:materials')

    def test_func(self):
        content = self.get_object()
        return self.request.user == content.uploaded_by or self.request.user.is_staff
