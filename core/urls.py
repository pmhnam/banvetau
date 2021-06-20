from django.urls import path, include
from . import views
from .views import Schedules, Tickets


urlpatterns = [
    path('schedules/', Schedules.as_view(), name='schedules'),
    path('', Tickets.as_view()),

    path('i/', views.index),
    # path('', views.chontuyen),
    # path('xyly', views.xyly),
]