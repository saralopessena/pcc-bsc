from django.db import models
from django.contrib.auth.models import User

class ProfilePicture(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Profile Picture', upload_to='profile', default='profile/unknown.png')

    def __str__(self):
        return self.user.username