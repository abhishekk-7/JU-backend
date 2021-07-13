from django.urls import path
from .views import ExploreView, ExploreDetailView

urlpatterns = [
    path('explore/', ExploreView.as_view(), name='explore'),
    path('explore/<int:id>', ExploreDetailView.as_view(), name='exploredetail'),
]
