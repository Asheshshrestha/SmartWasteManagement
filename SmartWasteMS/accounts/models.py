from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    citizen_no=models.IntegerField(unique=True)
    image = models.ImageField(upload_to='accounts/usersimage',default="")
    age=models.IntegerField()
    gender =models.CharField(max_length=255)
    address = models.CharField(max_length=225)
    van_no=models.IntegerField()

    def __str__(self):
        return self.user.username
    

    

   

    