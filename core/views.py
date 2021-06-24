from django.shortcuts import render, redirect
from .models import User,Bill,BillDetail,Ticket,Train,Schedule,Route,Station
from datetime import date,datetime as datetime2
from django.views import View
from django.db.models import Q
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegistrationForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


@login_required
def index(request):
    list_bill_detail = []
    today = date.today()
    now = datetime2.now() + datetime.timedelta(hours = 2)
    current_time_txt = now.strftime("%H:%M:%S")
    current_time = datetime2.strptime(current_time_txt,"%H:%M:%S").time()

    bills = Bill.objects.filter(user = request.user)
    for bill in bills:
        bdts = BillDetail.objects.filter(bill = bill)
        for bdt in bdts:
            if bdt.ticket.schedule.start_day == today:
                if bdt.ticket.schedule.start_time > current_time:
                    list_bill_detail.append(bdt)
            elif bdt.ticket.schedule.start_day > today:
                list_bill_detail.append(bdt)
    number = len(list_bill_detail)
    context = {
        'list_bill_detail':list_bill_detail,
        'number':number,
    }
    return render(request, "core/index.html",context)

def register(request):
    form =RegistrationForm()
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'core/register.html',{'form':form})


@login_required
def ticketDetail(request,pk):
    bill_detail = BillDetail.objects.get(pk = pk)
    # bill_detail = BillDetail.objects.get(pk = pk)
    context = {
        'bill_detail':bill_detail,
    }
    return render(request, 'core/ticket_detail.html',context)

# bill_detail.id cho manage
@login_required
def huyVe(request,pk):
    bill_detail = BillDetail.objects.get(pk = pk)
    bill = Bill.objects.get(id = bill_detail.bill.id)
    ticket = Ticket.objects.get(id = bill_detail.ticket.id)
    ticket.status = 'F'
    bill.total -= ticket.cost
    ticket.save()
    bill.save()
    bill_detail.delete()
    return redirect(request.META.get('HTTP_REFERER'))



@login_required
def thanhToan(request):
    bill = Bill.objects.filter(user = request.user, status = 'UNPAID').first()
    if(bill != None):
        bill_details = bill.bills.all()
    else:
        bill_details = None
    context= {
        'bill_details':bill_details,
        'bill':bill,
    }
    return render(request, 'core/thanhtoan.html',context)

@login_required
def xuLyThanhToan(request,pk):
    bill = Bill.objects.get(pk = pk)
    bill.status = 'PAID'
    bill.save()
    return redirect(request.META.get('HTTP_REFERER'))


# @method_decorator(login_required(), name='dispatch')
class Tickets(View):
    def get(self,request):
        today = date.today()
        now = datetime2.now()
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
                print("id vé đặt là ",id)
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
        return redirect('index')


@method_decorator(staff_member_required, name='dispatch')
class Schedules(View):
    def get(self,request):
        trains = Train.objects.all()
        routes = Route.objects.all()
        schedules = Schedule.objects.all().order_by('-start_day')
        context = {
            'schedules':schedules,
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
    

@method_decorator(staff_member_required, name='dispatch')
class Routes(View):
    def get(self,request):
        stations = Station.objects.all()
        routes = Route.objects.all()
        context = {
            'stations':stations,
            'routes':routes,
        }
        return render(request, 'core/routes.html',context)
    
    def post(self,request):
        form = request.POST
        departure_id = form['departure']
        destination_id = form['destination']
        departure = Station.objects.get(id = departure_id )
        destination = Station.objects.get(id = destination_id )

        obj, created = Route.objects.get_or_create(departure = departure,destination = destination )
        return redirect("routes")
    

@method_decorator(staff_member_required, name='dispatch')
class Stations(View):
    def get(self,request):
        stations = Station.objects.all()
        context = {
            'stations':stations,
        }
        return render(request, 'core/stations.html',context)
    
    def post(self,request):
        form = request.POST
        name = form['name']
        address = form['address']

        Station.objects.get_or_create(name = name, address = address )
        return redirect("stations")


@method_decorator(staff_member_required, name='dispatch')
class Trains(View):
    def get(self,request):
        trains = Train.objects.all()
        context = {
            'trains':trains,
        }
        return render(request, 'core/trains.html',context)
    
    def post(self,request):
        form = request.POST
        name = form['name']
        capacity = form['capacity']

        Train.objects.get_or_create(name = name, capacity = capacity )
        return redirect("trains")
    
@staff_member_required
def get_bill(request):
    bills = Bill.objects.all().order_by('-status','-date')
    context = {
        'bills':bills,
    }
    return render(request,'core/bills.html',context)

@staff_member_required
def detail_bill(request,pk):
    bill = Bill.objects.get(pk=pk)
    bill_details = bill.bills.all()
    context = {
        'bill':bill,
        'bill_details':bill_details,
    }
    return render(request,'core/bill_details.html',context)


        