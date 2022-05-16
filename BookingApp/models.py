import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ReservationAvail(models.Model):

    STATUS = ((0, "Closed"), (1, "Open"))
    restaurant_status = models.IntegerField(default=1, choices=STATUS)  
    tables_available = models.IntegerField()


class Reservation(models.Model):
    AVAILABLE_GROUPS = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8')
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField(blank=True)
    party_size = models.IntegerField(choices=AVAILABLE_GROUPS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(ReservationAvail, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    end_reservation = datetime.timedelta(seconds=10800)
    message = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} has made a reservation for {self.party_size} people on {self.date_and_time}.'
