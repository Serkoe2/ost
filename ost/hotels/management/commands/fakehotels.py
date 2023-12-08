from django.core.management.base import BaseCommand
from faker.generator import random

from hotels.models import Hotel, AdditionalService, Room
from django_seed import Seed

seeder = Seed.seeder("ru_RU")


class Command(BaseCommand):
    help = 'Загружает начальные данные в базу данных'

    def add_arguments(self, parser):
        parser.add_argument("count", nargs="+", type=int)

    def handle(self, *args, **options):
        if 'count' in options:
            count = options['count'].pop()
        else:
            count = 10

        self.fake_hotels(count)
        self.fake_services(count)
        self.fake_rooms(count)
        seeder.execute()


    def fake_hotels(self, count):
        seeder.add_entity(Hotel, count, {
            'name': lambda x: seeder.faker.company(),
            'address': lambda x: seeder.faker.address(),
            'airport_distance': lambda x: random.random() * 50,
            'train_station_distance': lambda x: random.random() * 50,
            'bus_station_distance': lambda x: random.random() * 50,
            'rating': lambda x: random.random() * 10
        })

    def fake_services(self, count):
        seeder.add_entity(AdditionalService, count, {
            'name': lambda x: random.choice(["Завтрак", "Обед", "Экскурсии", "Уборка номера"]),
            'is_paid': lambda x: random.choice([True, False]),
        })

    def fake_rooms(self, count):
        seeder.add_entity(Room, count, {
            'room_type': lambda x: random.choice(["Simple", "Simple+", "Comfort", "Deluxe"]),
            'price_per_night': lambda x: random.choice([True, False]),
            'schedule': ""
        })
