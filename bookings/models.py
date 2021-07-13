from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.


class Ticket(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    # time = models.TimeField()
    place = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        validators=[MaxValueValidator(4)], default=1)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
