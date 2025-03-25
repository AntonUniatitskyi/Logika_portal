from django.urls import path
from . import views

app_name = 'voting'

urlpatterns = [
    # Шаблони для основного опитування
    path('polls/', views.poll_list, name='poll_list'),
    path('poll/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/results/', views.poll_results, name='poll_results'),

    # Нові маршрути для опитування учнів:
    path('student-poll/', views.poll_step, name='poll_step'),  # Крок опитування
    path('student-poll/final/', views.poll_final, name='poll_final'),  # Фінальна сторінка
]