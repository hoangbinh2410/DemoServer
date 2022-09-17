from demoapi.models import *
from .serializer import *
import logging
import random
from django_cron import CronJobBase, Schedule

def my_scheduled_job():
    val = random.randint(1, 1000)
    output = {
        "makhoa": val,
        "tenkhoa" : val,
        "dienthoai": val      
    }
    request = TBLKhoa.objects.get_or_create(**output)   
    print(request)