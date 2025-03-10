from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.MaterialListView.as_view(), name='materials'),
    path('update/<int:pk>/', views.MaterialUpdateView.as_view(), name='update_material'),
    path('delete/<int:pk>/', views.MaterialDeleteView.as_view(), name='delete_material'),
]
