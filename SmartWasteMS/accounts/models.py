from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='',
                              null=True, blank=True,
                              width_field='width_field',
                              height_field='height_field')
    height_field = models.IntegerField(default=0,blank=True,null=True)
    width_field = models.IntegerField(default=0,blank=True,null=True)
    name = models.CharField(max_length=30,default="Enter your name")
    extra_info=models.CharField(max_length=100,default='',blank=True,null=True)
    driver_address = models.TextField(max_length=1000, default='',blank=True,null=True)
    mobile=models.CharField(max_length=15,blank=True,null=True)
    vehicle=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return str(self.driver_id.username)

class Staff(models.Model):
    staff_id=models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='',
                              null=True, blank=True,
                              width_field='width_field',
                              height_field='height_field')
    height_field = models.IntegerField(default=0,blank=True,null=True)
    width_field = models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(max_length=30,default="Enter your name")
    staff_address = models.TextField(max_length=1000, default="",blank=True,null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)


    extra_info=models.CharField(max_length=100,default='',blank=True,null=True)

    def __str__(self):
        return str(self.staff_id.username)
    

   

    