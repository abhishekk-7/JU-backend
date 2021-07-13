from django.shortcuts import render
from .models import Ticket
from .serializers import BookingSerializer, TicketSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from .models import Ticket, Bookings
# Create your views here.


class AvailableTickets(GenericAPIView, ListModelMixin):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.filter(available=True)
    print(queryset)

    def get(self, request):
        return self.list(request)


class TicketView(GenericAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"ticket": "success"}, status=201)


class TicketHistoryView(GenericAPIView, ListModelMixin):
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        return Bookings.objects.filter(user=user)

    def get(self, request):
        return self.list(request)


class BookingView(GenericAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book = Bookings.objects.create(user=request.user, quantity=request.data.get(
            'quantity'), ticket=Ticket(request.data.get('ticket')))
        serializer = BookingSerializer(book)
        return Response(serializer.data)
