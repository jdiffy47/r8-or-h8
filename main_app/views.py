from django.shortcuts import render, redirect
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

def add_rating(request, bar_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.bar_id = bar_id
    new_rating.save()
  return redirect('bars_detail', bar_id=bar_id)

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
