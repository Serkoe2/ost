from django.contrib import admin
from django.urls import include, path
from django_prometheus import exports
from rest_framework import routers

from hotels import views

router = routers.DefaultRouter()
router.register(r'hotels', views.HotelViewSet, basename='hotel')
router.register(r'service', views.HotelServiceViewSet, basename='additionalservice')
router.register(r'room', views.HotelRoomViewSet, basename='room')
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path("metrics", exports.ExportToDjangoView, name="prometheus-django-metrics")
]
