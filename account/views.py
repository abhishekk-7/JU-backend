from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import response
from rest_framework.serializers import Serializer
from .serializers import PlaceSerializer, UserSerializer, FeedbackSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Feedback, Places
# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        places = ["Jal Mahal", "Nahargarh", "Jantar Mantar"]
        serializer = UserSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['username'] = request.data.get('email')
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()
        for place in places:
            Places.objects.create(user=user, place=place)
        return Response({"token": Token.objects.create(user=user).key}, status=201)


class LoginView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        if request.user.is_authenticated:
            token = Token.objects.get(user=request.user)
            return Response({
                "success": True,
                "user": UserSerializer(request.user).data,
                "token": token.key
            }, status=201)
        else:
            return Response({
                "success": False,
            }, status=201)


class FeedbackView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer

    def post(self, request):
        feed = Feedback.objects.create(user=request.user, title=request.data.get(
            'title'), body=request.data.get('body'))
        serializer = FeedbackSerializer(feed)
        return Response({"feedback": "success"}, status=201)


class PlacesView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Places.objects.filter(user=user)

    def get(self, request, id=None):
        return self.list(request)

    def put(self, request, id):
        return self.update(request, id=id)


class LoggedIn(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        if request.user.is_authenticated:
            token = Token.objects.get(user=request.user)
            return Response({
                "success": True,
                "user": UserSerializer(request.user).data,
                "token": token.key
            }, status=201)
        else:
            return Response({
                "success": False,
            }, status=400)


class UserDetails(generics.GenericAPIView):
    def post(self, request):
        print(request.data['Token'])
        user_id = Token.objects.get(key=request.data['Token']).user_id
        user = User.objects.get(id=user_id)
        print(user.first_name)
        return JsonResponse({'user': user.first_name})
