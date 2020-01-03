import os
from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab





# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trashcan.settings')

app = Celery('trashcan')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@periodic_task(run_every=crontab(minute="*"))
def schedule_task():
    from bin.models import dustbin,stat_count
    n=0
    f=0
    h=0
    e=0
    t=0
    
    bins = dustbin.objects.all()
    
    for i in bins:
        if i.bin_status==-1:
            n=n+1
        elif i.bin_status>30:
            f=f+1
        elif i.bin_status>100:
            h=h+1
        elif i.bin_status>150:
            e = e+1
        else:

            t=t+1
    b = stat_count(full_bin=f,empty_bin=e,half_bin=h)
    b.save()


    
        
