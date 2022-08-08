from django.shortcuts import render
from .models import Bar



# class Bar:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, area, description):
#     self.name = name
#     self.area = area
#     self.description = description

# bars = [
#   Bar('Tellus360', 'Lancaster PA', '3 story building with rooftop'),
#   Bar('Marion Court', 'Lancaster PA', 'Go here if you want to get shot or kicked out'),
#   Bar('Decades', 'Lancaster PA', 'Gaming bar with arcade and bowling'),
# ]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/index.html', { 'bars': bars })
