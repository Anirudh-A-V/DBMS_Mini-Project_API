from django.db import models

# Create your models here.

class Consumer(models.Model):
    consumer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    consumer_id = models.ForeignKey(Consumer, on_delete=models.DO_NOTHING)
    units = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return Consumer.objects.get(consumer_id=self.consumer_id).username + " " + str(self.date)

class BillStatus(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100)

    def __str__(self):
        return Consumer.objects.get(consumer_id=Bill.objects.get(bill_id=self.bill_id).consumer_id).username + " " + self.status

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    consumer_id = models.ForeignKey(Consumer, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return Consumer.objects.get(consumer_id=self.consumer_id).username + " " + str(self.date)