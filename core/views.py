from django.shortcuts import render
from .models import User,Bill,BillDetail,Ticket,Train,Schedule,Route,Station

# Create your views here.

def index(request):
    train = Train.objects.get(id = 1)
    for i in range(1,51):
        obj, created = Ticket.objects.get_or_create(seat = i, cost = 100000, train = train)
    return render(request, "core/index.html")