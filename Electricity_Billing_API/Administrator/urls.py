from django.urls import path, include
from rest_framework import routers
from .views import AdminViewSet

router = routers.DefaultRouter()

router.register("administrator", AdminViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]