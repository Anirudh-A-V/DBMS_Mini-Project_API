from django.contrib import admin
from .models import Consumer, Bill, BillStatus, Complaint
# Register your models here.

admin.site.register(Consumer)
admin.site.register(Bill)
admin.site.register(BillStatus)
admin.site.register(Complaint)
