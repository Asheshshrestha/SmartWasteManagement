from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class notice(models.Model):
    CHOOSE=(("1","all"),("2","Admin"),("2","Staff"))
    title = models.CharField(max_length=225)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    message = models.TextField()
    notice_to = models.CharField(choices =CHOOSE,max_length=5)
    notice_date=models.DateField()
    notice_time = models.TimeField()
    

