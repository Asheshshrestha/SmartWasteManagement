import datetime
from celery import task

celery = Celery('tasks', broker='amqp://127.0.0.1:8080') #!

import os

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "trashcan.settings"
@task
def update_dustbin_chart(request):
    print("ashesh")
    bins= dustbin.objects.all()
    full=0
    half=0
    empty=0
    t=0
    n=0
    for i in bins:
        if i.bin_status==-1:
            n=n+1
        elif i.bin_status<30:
            full=full+1
        elif i.bin_status<100:
            half=half+1
        elif i.bin_status<150:
            empty = empty+1
        else:

            t=t+1
    try:
        new_status = stat_count()
            
            # open weather map gives temps in Kelvin. We want celsius.              
            

        new_status.full_bin = full
        new_status.half_bin = half
        new_status.empty_bin = empty
        new_status.date_time = datetime.datetime.now()
        new_status.save()
    except:
        pass
    return HttpResponse("upated")
         