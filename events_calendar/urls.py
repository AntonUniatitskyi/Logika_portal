from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar_week'),
]
