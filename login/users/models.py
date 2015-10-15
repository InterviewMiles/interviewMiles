from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    contact_no = models.BigIntegerField(null=True,blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return "Hello "+self.user.first_name+" !!"

class UserResponce(models.Model):
    result = models.CharField(max_length=100)
    def __init__(self,val):
        self.result = val