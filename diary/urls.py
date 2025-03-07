from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('diary', views.DiaryView.as_view(), name='diary'),
    path('edit-mark/<int:pk>/', views.MarkUpdateView.as_view(), name='edit_mark'),
    path('delete-mark/<int:pk>/', views.MarkDeleteView.as_view(), name='delete_mark')
]