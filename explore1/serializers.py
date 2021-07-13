from django.db import models
from . models import Explore
from rest_framework.serializers import ModelSerializer


class ExploreSerializer(ModelSerializer):

    class Meta:
        model = Explore
        fields = '__all__'
