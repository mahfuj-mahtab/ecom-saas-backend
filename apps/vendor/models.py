from django.db import models
from django.contrib.auth.models import User
from org.models import *
# Create your models here.
class vendor(models.Model):
    status = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
        ('SUSPEND', 'SUSPEND'),
    )
    name = models.CharField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    org = models.ForeignKey(Organization,on_delete=models.CASCADE)
    description = models.TextField(max_length=  1000)
    logo = models.ImageField(upload_to="/media/upload/")
    contact_info = models.CharField()
    status = models.CharField(choices=status, default='INACTIVE')
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.name