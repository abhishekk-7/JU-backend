from blog2.serializers import BlogSerializer
from blog2.models import Blog
from rest_framework import generics, mixins
from bookings.models import Ticket
from bookings.serializers import TicketSerializer

# Create your views here.


class LatestBlog(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter().order_by('-created')[: 3]

    def get(self, request):
        return self.list(request)


class AllTIckets(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    lookup_field = 'id'

    def get(self, request, id=id):
        return self.retrieve(request)
