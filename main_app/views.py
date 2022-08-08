from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bar



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/index.html', { 'bars': bars })

def bars_detail(request, bar_id):
  bar = Bar.objects.get(id=bar_id)
  return render(request, 'bars/detail.html', { 'bar': bar })

class BarCreate(CreateView):
  model = Bar
  fields = '__all__'
