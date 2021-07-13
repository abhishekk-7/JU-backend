from django.shortcuts import render
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny
# Create your views here.


class BlogView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get(self, request):
        return self.list(request)


class BlogDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'id'

    def get(self, request, id=id):
        return self.retrieve(request)
