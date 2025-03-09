from datetime import datetime,timedelta
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
class CalendarView(LoginRequiredMixin,ListView):
    model =  models.Event
    template_name = "calendar/calendar.html"
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.today().date()
        context["week"] =[0,1,2,3,4,5,6]
        context["start_of_week"] = context["today"] - timedelta(days=context["today"].weekday())  # понедельник текущей недели
        context["end_of_week"] = context["start_of_week"] + timedelta(days=6)
        return context
