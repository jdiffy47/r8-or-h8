from django.contrib import admin
from .models import Bar, Rating, Beverage
# Register your models here.
admin.site.register(Bar)
admin.site.register(Rating)
admin.site.register(Beverage)

