from django.urls import path
from .views import LatestBlog, AllTIckets

urlpatterns = [
    path('latest/', LatestBlog.as_view(), name='latest'),
    path('tickets', AllTIckets.as_view(), name='tickets'),
]
