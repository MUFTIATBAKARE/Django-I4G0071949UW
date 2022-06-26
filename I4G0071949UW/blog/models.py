from django.db import models
from django.conf import settings
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Created_date = models.DateTimeField()
    Published_date  = models.DateTimeField()
    author = author = models.ForeignKey(get_user_model())