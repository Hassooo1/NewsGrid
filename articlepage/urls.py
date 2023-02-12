from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='article'),
    path('createarticles/', views.createarticle, name='createarticles'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
