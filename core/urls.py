from django.urls import path, include
from . import views
from .views import Schedules, Tickets
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('schedules/', Schedules.as_view(), name='schedules'),
    path('datve/', Tickets.as_view(), name='datve'),
    path('', views.index,name = 'index'),
    path('detail/<int:pk>',views.ticketDetail, name="ticket_detail"),
    path('huyve/<int:pk>',views.huyVe, name="huyve"),
    path('thanhtoan/',views.thanhToan, name="thanhtoan"),
    path('thanhtoan/<int:pk>',views.xuLyThanhToan, name="xulythanhtoan"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('register/', views.register , name='register'),

]