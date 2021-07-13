from django.shortcuts import render
from .serializers import ExploreSerializer
from .models import Explore
from rest_framework import generics, mixins
# Create your views here.


class ExploreView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ExploreSerializer
    queryset = Explore.objects.all()

    def get(self, request):
        return self.list(request)


class ExploreDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ExploreSerializer
    queryset = Explore.objects.all()
    lookup_field = 'id'

    def get(self, request, id=id):
        return self.retrieve(request)
