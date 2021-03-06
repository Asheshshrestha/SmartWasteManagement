from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from bin.models import Area
from datetime import datetime 


class UserProfile(models.Model):
    CHOICES =(("male","male"),("female","female"),("others","others"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no =models.IntegerField(null=True)
    image = models.ImageField(upload_to='accounts/usersimage',default="profile.jpg")
    age=models.IntegerField(null=True)
    gender =models.CharField(max_length=6,default="N/A",choices=CHOICES)
    address = models.CharField(max_length=225,default="N/A")
    van_no=models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.username} UserProfile'



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile, sender=User)

    
class Task_done(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date_time = models.DateTimeField( null=True)
    area = models.ForeignKey(Area,on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.user.username}_{self.area}_{self.date_time}'





   

    