from django.db import models
from django.contrib.auth.models import User

# Create your models here.


     
class Area(models.Model):
    area_name = models.CharField(max_length=50,unique=True)
    area_logitude = models.FloatField(null=True)
    area_latitude = models.FloatField(null=True)
    assigned_user = models.ForeignKey(User,related_name="area_assigned_user",on_delete=models.SET_NULL,null=True)

    
    def __str__(self):
        return self.area_name

class street(models.Model):
    street_name = models.CharField(max_length = 50,unique=True)
    street_area = models.ForeignKey(Area,on_delete=models.SET_NULL,null=True)
    assigned_user = models.ForeignKey(User,related_name="street_assigned_user",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.street_name

class dustbin(models.Model):
    bin_no = models.IntegerField(primary_key=True)
    added_by = models.ForeignKey(User,related_name="added_by",on_delete=models.SET_NULL,null=True)
    assigned_user = models.ForeignKey(User,related_name="assigned_user",on_delete=models.SET_NULL,null=True)
    bin_area = models.ForeignKey(Area,on_delete=models.SET_NULL,null=True)
    bin_street = models.ForeignKey(street,on_delete=models.SET_NULL,null=True)
    bin_logitude = models.FloatField()
    bin_latitude = models.FloatField()
    bin_status = models.IntegerField(default=-1) 
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,related_name="updated_by",on_delete=models.SET_NULL,null=True)

    
    def __str__(self):
        return 'bin'+str(self.bin_no)
class stat_count(models.Model):

    full_bin=models.IntegerField()
    empty_bin= models.IntegerField()
    half_bin = models.IntegerField()
    date_time = models.DateTimeField()


