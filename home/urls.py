from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('newsletter/subscribe', views.subscribe, name='subscribe'),
    path("newsletter/unsubscribe", views.unsubscribe, name="unsubscribe"),
]
