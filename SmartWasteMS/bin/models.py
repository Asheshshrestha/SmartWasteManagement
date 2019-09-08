from django.db import models

# Create your models here.
class dustbin(models.Model):
    bin_no = models.IntegerField(primary_key=True)
    bin_area = models.CharField( max_length=50)
    bin_street = models.CharField( max_length=50)
    bin_logitude = models.FloatField()
    bin_latitude = models.FloatField()
    bin_status = models.IntegerField(default=-1)
    
    def __str__(self):
        return 'bin'+str(self.bin_no)

