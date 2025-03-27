from datetime import datetime,timedelta
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import EventForm
from django.db.models import Q
from home.models import Group

# Create your views here.
class CalendarView(LoginRequiredMixin, ListView):
    model = models.Event
    template_name = "calendar/calendar.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        queryset = queryset.filter(Q(created_by=self.request.user) | Q(group__user=self.request.user))

        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')

        if year and month and day:
            current_date = datetime(year, month, day).date()
        else:
            current_date = datetime.today().date()

        start_of_week = current_date - timedelta(days=current_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = queryset.filter(date__range=[start_of_week, end_of_week])
        queryset = queryset.order_by('start_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')

        if year and month and day:
            current_date = datetime(year, month, day).date()
        else:
            current_date = datetime.today().date()

        context["today"] = current_date
        context["week"] = [0, 1, 2, 3, 4, 5, 6]
        context["weekdays"] = ['Понеділок', "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        context["start_of_week"] = current_date - timedelta(days=current_date.weekday())
        context["end_of_week"] = context["start_of_week"] + timedelta(days=6)

        context["prev_week_url"] = self.get_week_url(current_date, -7)
        context["next_week_url"] = self.get_week_url(current_date, 7)

        # Додаємо інформацію про поточний тиждень
        today_date = datetime.today().date()
        context["is_current_week"] = (
                current_date.weekday() == today_date.weekday() and
                current_date.month == today_date.month and
                current_date.year == today_date.year and
                context["start_of_week"] == today_date - timedelta(days=today_date.weekday())
            )
        # Форма додавання події
        if self.request.user.has_perm('Events_Calendar.view_event'):
            context['add_event'] = EventForm()
        else:
            context['add_event'] = None

        return context

    def get_week_url(self, current_date, delta):
        new_date = current_date + timedelta(days=delta)
        return f"/calendar/{new_date.year}/{new_date.month}/{new_date.day}/"

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)  # Не сохраняем сразу, проверяем
            event.created_by = self.request.user

            if event.start_time:
                end_time = (datetime.combine(event.date, event.start_time) + timedelta(hours=1)).time()
            
            overlapping_events = models.Event.objects.filter(
                date=event.date,  
                start_time__lt=end_time,  
                end_time__gt=event.start_time  ,
                group = event.group
            )

            if not overlapping_events:
                event.save()
                messages.success(request, "Подію додано, перегляньте сторінку.")
                return redirect('calendar:calendar')
            messages.error(request, "Час зайнятий! Оберіть інший.")
            return redirect('calendar:calendar')
            