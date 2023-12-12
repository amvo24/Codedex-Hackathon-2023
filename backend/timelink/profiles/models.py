from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserProfile(models.Model):
    # creating one to one relationship with predefined Django user model.
    user = models.OneToOneField(User, on_delete=models.CASCADE) # allows for creation/deletion
    dob = models.DateField(null=True, blank=True, default=date.today) # if user wants to add DOB
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True) # come back to it
    def __str__(self): # debugging use only. To call back and see what it does.
        return self.user.username