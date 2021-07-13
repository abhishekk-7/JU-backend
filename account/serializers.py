from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Feedback, Places


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'username', 'password')
        extra_kwargs = {'username': {'required': False}}


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('title', 'body')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ('place', 'done', 'id')
