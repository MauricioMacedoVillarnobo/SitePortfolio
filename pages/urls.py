# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre/', views.about_view, name='about'),
    path('ferramentas/', views.tools_view, name='tools'),
    path('contato/', views.contact_view, name='contact'),
]
