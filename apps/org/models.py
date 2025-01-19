from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Organization(models.Model):
    name = models.TextField(max_length=250)
    description = models.TextField(max_length=1000)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    sub_domain = models.CharField()
    is_multivendor = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='/media/upload/')
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name