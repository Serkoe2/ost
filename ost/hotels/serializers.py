from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Hotel, AdditionalService, Room


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['url',
                  'name',
                  'address',
                  'airport_distance',
                  'train_station_distance',
                  'bus_station_distance']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdditionalService
        fields = '__all__'


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
