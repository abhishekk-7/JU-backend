from django.urls import path
from .views import BookingView, TicketHistoryView, TicketView, AvailableTickets
urlpatterns = [
    path('bookings/', TicketHistoryView.as_view(), name='bookings'),
    path('ticket/', TicketView.as_view(), name='ticket'),
    path('book/', BookingView.as_view(), name='book'),
    path('alltickets/', AvailableTickets.as_view(), name='tickets'),
]
