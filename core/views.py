from django.shortcuts import render, redirect
from .models import User,Bill,BillDetail,Ticket,Train,Schedule,Route,Station
from datetime import date,datetime as datetime2
from django.views import View
from django.db.models import Q
import datetime

# Create your views here.

def index(request):
    list_ticket = []
    today = date.today()
    print(today)
    now = datetime2.now() + datetime.timedelta(hours = 2)
    current_time_txt = now.strftime("%H:%M:%S")
    current_time = datetime2.strptime(current_time_txt,"%H:%M:%S").time()
    

    bills = Bill.objects.filter(user = request.user)
    for bill in bills:
        bdts = BillDetail.objects.filter(bill = bill)
        for bdt in bdts:
            if bdt.ticket.schedule.start_day >= today and bdt.ticket.schedule.start_time > current_time :
                list_ticket.append(bdt.ticket)
    context = {
        'list_ticket':list_ticket,
    }
    return render(request, "core/index.html",context)


class Schedules(View):
    def get(self,request):
        trains = Train.objects.all()
        routes = Route.objects.all()
        context = {
            'trains':trains,
            'routes':routes,
        }
        return render(request, 'core/schedules.html',context)
    
    def post(self,request):
        form = request.POST
        train_id = form['train']
        route_id = form['route']
        start_day = form['start_day']
        start_time = form['start_time']

        print(start_time)
        train = Train.objects.get(id = train_id)
        route = Route.objects.get(id = route_id)
        obj, created = Schedule.objects.get_or_create(train = train,route = route, start_day = start_day, start_time = start_time)

        for i in range(1,31):
            Ticket.objects.get_or_create(seat = i, schedule = obj )
        
        return redirect("schedules")

    

def chontuyen(request):

    return render(request, 'core/test.html')
def xyly(request):
    a = Route.objects.all()
    a.txt
    return render(request, 'core/test.html')
    


class Tickets(View):
    def get(self,request):
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        schedules = Schedule.objects.filter(Q(start_day__gt = today) | Q(start_day = today , start_time__gt = current_time))
        fullticket = []
        for i in schedules:
            print(i)
            tickets = Ticket.objects.filter(schedule = i)
            for j in tickets:
                fullticket.append(j)
        routes = Route.objects.all()
        context = {
            'fullticket':fullticket,
            'schedules':schedules,
            'routes':routes,
        }
        return render(request,'core/timve.html',context)

    def post(self,request):
        print("da nhan du lieu")
        current_user = request.user
        form = request.POST
        tickets = Ticket.objects.filter(status = 'F')
        today = date.today()

        for i in tickets:
            id = form.get(str(i.id), None)
            if id != None:
                bill, created = Bill.objects.get_or_create(user = current_user,
                    status = 'UNPAID',
                    defaults={
                        "date" : today,
                    }
                )
                BillDetail.objects.get_or_create(bill = bill, ticket = i)
                i.status = 'T'
                i.save()
        total = 0
        for i in bill.bills.all():
            total += i.ticket.cost
        bill.total = total
        bill.save()
        return redirect('/')


