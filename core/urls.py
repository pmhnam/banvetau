from django.urls import path, include
from . import views
from .views import Schedules, Tickets, Routes, Stations, Trains
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.index,name = 'index'),
    path('detail/<int:pk>',views.ticketDetail, name="ticket_detail"),
    path('huyve/<int:pk>',views.huyVe, name="huyve"),
    path('', Tickets.as_view(), name='datve'),
    path('thanhtoan/',views.thanhToan, name="thanhtoan"),
    path('thanhtoan/<int:pk>/',views.xuLyThanhToan, name="xulythanhtoan"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('register/', views.register , name='register'),

    path('schedules/', Schedules.as_view(), name='schedules'),
    path('routes/', Routes.as_view() , name='routes'),
    path('stations/', Stations.as_view() , name='stations'),
    path('trains/', Trains.as_view() , name='trains'),
    path('bills/', views.get_bill , name='bills'),
    path('detail-bills/<int:pk>/', views.detail_bill , name='detail_bill'),
]