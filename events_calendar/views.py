from datetime import datetime,timedelta
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
class CalendarView(LoginRequiredMixin, ListView):
    model = models.Event
    template_name = "calendar/calendar.html"
    context_object_name = 'events'
    ordering = 'start_time'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')

        if year and month and day:
            current_date = datetime(year, month, day).date()
        else:
            current_date = datetime.today().date()

        start_of_week = current_date - timedelta(days=current_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = models.Event.objects.filter(date__range=[start_of_week, end_of_week])
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
        return context

    def get_week_url(self, current_date, delta):
        new_date = current_date + timedelta(days=delta)
        return f"/calendar/{new_date.year}/{new_date.month}/{new_date.day}/"
