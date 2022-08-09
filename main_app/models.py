from django.db import models
from django.urls import reverse
from datetime import date


RATES = (
  ('1', '⭐'),
  ('2', '⭐⭐'),
  ('3', '⭐⭐⭐'),
  ('4', '⭐⭐⭐⭐'),
  ('5', '⭐⭐⭐⭐⭐'),
)
# Create your models here.
class Bar(models.Model):
  name = models.CharField(max_length=100)
  area = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('bars_detail', kwargs={'bar_id': self.id})


class Rating(models.Model):
  date = models.DateField('Rating date')
  rate = models.CharField(max_length=1, choices=RATES, default=RATES[0][0])
  description = models.TextField(max_length=250)

  bar = models.ForeignKey(Bar, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_rate_display()} on {self.date}"

  def __str__(self):
    return self.description

class Meta:
  ordering = ['-date']

# Add the Toy model
class Beverage(models.Model):
  name = models.CharField(max_length=50)
  dankness = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('beverages_detail', kwargs={'pk': self.id})