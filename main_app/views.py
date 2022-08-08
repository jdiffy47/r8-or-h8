from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bar
from .forms import RatingForm



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/index.html', { 'bars': bars })

def bars_detail(request, bar_id):
  bar = Bar.objects.get(id=bar_id)
  rating_form = RatingForm()
  return render(request, 'bars/detail.html', { 'bar': bar, 'rating_form': rating_form })

class BarCreate(CreateView):
  model = Bar
  fields = '__all__'
  success_url = '/bars/'

class BarUpdate(UpdateView):
  model = Bar
  fields = ['name', 'area', 'description']

class BarDelete(DeleteView):
  model = Bar
  success_url = '/bars/'
