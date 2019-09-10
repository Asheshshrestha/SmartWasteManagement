from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class dustbin(models.Model):
    bin_no = models.IntegerField(primary_key=True)
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    bin_area = models.CharField( max_length=50)
    bin_street = models.CharField( max_length=50)
    bin_logitude = models.FloatField()
    bin_latitude = models.FloatField()
    bin_status = models.IntegerField(default=-1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'bin'+str(self.bin_no)

