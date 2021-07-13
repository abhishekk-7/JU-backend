from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blogdetail'),
]