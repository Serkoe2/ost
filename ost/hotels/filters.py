import django_filters

from hotels.models import Hotel


class HotelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Hotel
        fields = {
            'airport_distance': ['lt', 'gt', 'exact', 'lte', 'gte'],
            'train_station_distance':['lt', 'gt', 'exact', 'lte', 'gte'],
            'bus_station_distance': ['lt', 'gt', 'exact', 'lte', 'gte'],
            'rating': ['lt', 'gt', 'exact', 'lte', 'gte']
        }
