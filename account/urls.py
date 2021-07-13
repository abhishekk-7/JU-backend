from django.urls import path
from .views import LoggedIn, RegisterView, LoginView, FeedbackView, PlacesView, UserDetails
from rest_framework.authtoken import views
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.obtain_auth_token, name='login'),
    path('feed/', FeedbackView.as_view(), name='feedback'),
    path('places/<int:id>', PlacesView.as_view(), name='placesid'),
    path('places/', PlacesView.as_view(), name='places'),
    path('loggedin/', LoggedIn.as_view(), name='loggedin'),
    path('details/', UserDetails.as_view(), name='details')
]
