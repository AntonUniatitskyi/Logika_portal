from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio-det/<int:pk>/', views.PortfolioDetail.as_view(), name='portfolio_deta'),
    path('create', views.PortfolioCreateView.as_view(), name='portfolio_create'),
    path('portfolio/edit/<int:pk>/', views.PortfolioUpdateView.as_view(), name='portfolio_edit'),

]

