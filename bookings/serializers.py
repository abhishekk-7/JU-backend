from django.db import models
from rest_framework.utils import field_mapping
from .models import Bookings, Ticket
from rest_framework import serializers
from account.serializers import UserSerializer


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Bookings
        fields = ('ticket', 'quantity')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
