from rest_framework import serializers

from .models import Consumer, Bill, BillStatus, Complaint

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = "__all__"

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

class BillStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillStatus
        fields = "__all__"

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = "__all__"

