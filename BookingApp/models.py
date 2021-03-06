from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    '''
    Utilized by both the Admin CMS as well as well as user-generated
    form input for creating and managing reservations.
    '''
    STATUS = ((0, "Unconfirmed"), (1, "Confirmed"))
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
    phone_number = models.BigIntegerField(blank=True, null=True)
    party_size = models.IntegerField(choices=AVAILABLE_GROUPS)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_status = models.IntegerField(default=0, choices=STATUS)

    def __str__(self):
        return f'{self.name}'
