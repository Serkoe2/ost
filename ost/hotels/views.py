from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User
from django_filters import rest_framework as filters

from .filters import HotelFilter
from .serializers import HotelSerializer, UserSerializer, ServiceSerializer, RoomSerializer
from .models import Hotel, AdditionalService, Room


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelFilter
    serializer_class = HotelSerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class HotelServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hotels to be viewed
    """
    queryset = AdditionalService.objects.all()
    serializer_class = ServiceSerializer


class HotelRoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hotels to be viewed
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
