from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.

STATUS_TICKET_CHOICE = (
    ("T","Đã bán"),
    ("F","Chưa bán"),
)

COST_CHOICE = (
    (100000,"Một trăm"),
    (200000,"Hai trăm"),
    (300000,"Ba trăm"),
)

SEAT_TICKET_CHOICE = (
    ( 0 , "Seat 0" ),
    ( 1 , "Seat 1" ),
    ( 2 , "Seat 2" ),
    ( 3 , "Seat 3" ),
    ( 4 , "Seat 4" ),
    ( 5 , "Seat 5" ),
    ( 6 , "Seat 6" ),
    ( 7 , "Seat 7" ),
    ( 8 , "Seat 8" ),
    ( 9 , "Seat 9" ),
    ( 10, "Seat 10"),
    ( 11, "Seat 11"),
    ( 12, "Seat 12"),
    ( 13, "Seat 13"),
    ( 14, "Seat 14"),
    ( 15, "Seat 15"),
    ( 16, "Seat 16"),
    ( 17, "Seat 17"),
    ( 18, "Seat 18"),
    ( 19, "Seat 19"),
    ( 20, "Seat 20"),
    ( 21, "Seat 21"),
    ( 22, "Seat 22"),
    ( 23, "Seat 23"),
    ( 24, "Seat 24"),
    ( 25, "Seat 25"),
    ( 26, "Seat 26"),
    ( 27, "Seat 27"),
    ( 28, "Seat 28"),
    ( 29, "Seat 29"),
    ( 30, "Seat 30"),
    ( 31, "Seat 31"),
    ( 32, "Seat 32"),
    ( 33, "Seat 33"),
    ( 34, "Seat 34"),
    ( 35, "Seat 35"),
    ( 36, "Seat 36"),
    ( 37, "Seat 37"),
    ( 38, "Seat 38"),
    ( 39, "Seat 39"),
    ( 40, "Seat 40"),
    ( 41, "Seat 41"),
    ( 42, "Seat 42"),
    ( 43, "Seat 43"),
    ( 44, "Seat 44"),
    ( 45, "Seat 45"),
    ( 46, "Seat 46"),
    ( 47, "Seat 47"),
    ( 48, "Seat 48"),
    ( 49, "Seat 49"),
    ( 50, "Seat 50"),
)

TYPE_TICKET_CHOICE = (
    ('N', 'Normal'),
    ('V', 'VIP'),

)

STATUS_BILL_CHOICE = (
    ('PAID','Đã thanh toán'),
    ('DEPOSITED','Đã đặt cọc'),
    ('UNPAID','Chưa thanh toán'),
)


class Station(models.Model):
    name = models.CharField(default = "", max_length = 50)
    address = models.CharField(default = "",max_length = 255)

    def __str__(self) -> str:
        return self.name


class Route(models.Model):
    departure = models.ForeignKey(Station, related_name='stations_departure', on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, related_name='stations_destination', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.departure.name + " to " + self.destination.name


class Train(models.Model):
    name = models.CharField(default = "", max_length = 50)
    capacity = models.IntegerField(default = 50)
    place = models.CharField(default = "", max_length = 255, null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class Schedule(models.Model):
    train = models.ForeignKey(Train, related_name='trains', on_delete=models.CASCADE)
    start_day = models.DateTimeField(auto_now=False, auto_now_add=False)
    route = models.ForeignKey(Route, related_name='routes', on_delete=models.CASCADE)
    status = models.CharField(default = "", max_length=50, null=True,blank=True)

    def __str__(self) -> str:
        return str(self.start_day) + ", " + self.train.name + " from " + str(self.route)


class Ticket(models.Model):
    seat = models.IntegerField(choices = SEAT_TICKET_CHOICE)
    cost = models.IntegerField(choices = COST_CHOICE, default = 100000)
    type = models.CharField(choices = TYPE_TICKET_CHOICE, max_length=1, default='N')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name="trains_ticket")
    status = models.CharField(choices = STATUS_TICKET_CHOICE, default = 'F', max_length = 1)
 
    def __str__(self) -> str:
        return "ghế " + str(self.seat) + " " + self.train.name


class Bill(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    status = models.CharField(choices = STATUS_BILL_CHOICE, default="UNPAID", max_length=10)
 
    def __str__(self) -> str:
        return self.user.username + " on " + str(self.date)


class BillDetail(models.Model):
    bill = models.ForeignKey(Bill, related_name="bills", on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name="tickets", on_delete=models.CASCADE)
    status = models.CharField(default="", max_length = 50, null=True,blank=True)

    def __str__(self) -> str:
        return str(self.ticket) + " on " + str(self.bill)
