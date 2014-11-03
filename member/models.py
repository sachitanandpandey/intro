from django.db import models
#from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user            =models.OneToOneField(User)
    name            =models.CharField(max_length=100)
    email           =models.EmailField(max_length=200)
    Discription     =models.TextField(blank=True)


    def __unicode__(self):
        return self.name