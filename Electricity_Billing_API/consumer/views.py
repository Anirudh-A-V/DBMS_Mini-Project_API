from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .models import Consumer, Bill, BillStatus, Complaint
from .serializers import ConsumerSerializer, BillSerializer, BillStatusSerializer, ComplaintSerializer

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillStatusViewSet(viewsets.ModelViewSet):
    queryset = BillStatus.objects.all()
    serializer_class = BillStatusSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    