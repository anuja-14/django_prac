from django.db import models

# Create your models here.
#
#
#
class Page(models.Model):
     name = models.CharField(maxlength="20",primary_key=True)
     content=models.TextField(blank=True)


