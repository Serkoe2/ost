from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(unique=True)
    airport_distance = models.DecimalField(max_digits=5, decimal_places=2)
    train_station_distance = models.DecimalField(max_digits=5, decimal_places=2)
    bus_station_distance = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['airport_distance',
                                 'train_station_distance',
                                 'bus_station_distance'],
                         name='infra_idx'),
        ]


class AdditionalService(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='additional_services')
    name = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.TextField()
