from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Explore(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=10000)
    img_link = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.title
