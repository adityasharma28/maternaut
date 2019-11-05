from django.db import models
from django.contrib.auth.models import User


class user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=None, null=True, unique=True)
    location_lat = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True, null=True)
    location_lng = models.DecimalField(max_digits=10, decimal_places=6, default=None, blank=True, null=True)
    city = models.CharField(max_length=250, default=None, null=True, blank=True)
    child_count = models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return str(self.user)


