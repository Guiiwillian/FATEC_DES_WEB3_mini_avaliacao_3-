from django.urls import path
from . import views
urlpatterns = [
    path('natal', views.natal),
    path('tiradentes', views.tiradentes),
    path('', views.feriado),
]