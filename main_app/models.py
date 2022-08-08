from django.db import models
from django.urls import reverse

# Create your models here.
class Bar(models.Model):
  name = models.CharField(max_length=100)
  area = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('bars_detail', kwargs={'bar_id': self.id})