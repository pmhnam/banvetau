from django.contrib import admin
from .models import User,Bill,BillDetail,Ticket,Train,Schedule,Route,Station
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'username']
class BillAdmin(admin.ModelAdmin):
    list_display = ['user','total', 'date','status']
class BillDetailAdmin(admin.ModelAdmin):
    list_display = ['bill', 'ticket', 'status']
class TicketAdmin(admin.ModelAdmin):
    list_display = ['seat','status', 'cost', 'type', 'schedule']
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['train', 'start_day','route']
class TrainAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity','place']
class RouteAdmin(admin.ModelAdmin):
    list_display = ['departure', 'destination']
class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


# admin.site.register(User, UserAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(BillDetail, BillDetailAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Station, StationAdmin)
