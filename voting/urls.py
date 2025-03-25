from django.urls import path
from . import views

app_name = 'voting'

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('create/', views.create_poll, name='create_poll'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
]
