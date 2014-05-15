from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    property = models.CharField(max_length=100, blank=True, default='')
    value = models.TextField()
    
    
    class Meta:
        ordering = ('created',)
