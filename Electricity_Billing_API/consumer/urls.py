from django.urls import path, include
from rest_framework import routers
from .views import ConsumerViewSet, BillViewSet, BillStatusViewSet, ComplaintViewSet

router = routers.DefaultRouter()

router.register("consumer", ConsumerViewSet)
router.register("bill", BillViewSet)
router.register("billstatus", BillStatusViewSet)
router.register("complaint", ComplaintViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

