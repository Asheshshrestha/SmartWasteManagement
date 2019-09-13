from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    CHOICES =(("male","male"),("female","female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    citizen_no=models.IntegerField(null=True)
    image = models.ImageField(upload_to='accounts/usersimage',default="profile.jpg")
    age=models.IntegerField(null=True)
    gender =models.CharField(max_length=6,default="male",choices=CHOICES)
    address = models.CharField(max_length=225,null=True)
    van_no=models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.username} UserProfile'



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile, sender=User)

    

   

    