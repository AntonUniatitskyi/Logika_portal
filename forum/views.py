from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.db import models
from .models import Topic

class ForumTopicView(ListView):
    model = Topic
    template_name = "forum/forum.html"
    context_object_name = "topic_detail"

    def message(request):
        pass
