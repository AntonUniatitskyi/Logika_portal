from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .forms import MarkForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
class DiaryView(LoginRequiredMixin, ListView):
    model = models.Mark
    template_name = 'diary/diary.html'
    context_object_name = 'diary_detail'

    def get_queryset(self):
        if self.request.user.has_perm('diary.add_mark'):
            return models.Mark.objects.all().order_by('student__username', 'mark')
        return models.Mark.objects.filter(student=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_mark'] = self.get_queryset()
        context['has_add_mark_permission'] = self.request.user.has_perm('diary.add_mark')
        if context['has_add_mark_permission']:
            context['add_mark'] = MarkForm()
            context['add_mark'].fields['student'].queryset = User.objects.exclude(id=self.request.user.id)
        else: 
            context['add_mark'] = None
        return context
    
    def post(self, request, *args, **kwargs):
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Оцінку додано, перегляньте сторінку.')
            return redirect('diary:diary')
        return self.render_to_response(self.get_context_data(form=form))
    
class MarkUpdateView(UpdateView):
    model = models.Mark
    form_class = MarkForm
    template_name = 'diary/diary.html'
    success_url = reverse_lazy('diary:diary')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Оцінку успішно змінено")
        return response
    
class MarkDeleteView(DeleteView):
    model = models.Mark
    template_name = 'diary/delete_mark.html'
    success_url = reverse_lazy('diary:diary')