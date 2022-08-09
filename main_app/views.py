from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bar, Beverage
from .forms import RatingForm
from django.views.generic import ListView, DetailView



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/index.html', { 'bars': bars })

def bars_detail(request, bar_id):
  bar = Bar.objects.get(id=bar_id)
  beverages_bar_doesnt_have = Beverage.objects.exclude(id__in = bar.beverages.all().values_list('id'))
  rating_form = RatingForm()
  return render(request, 'bars/detail.html', { 'bar': bar, 'rating_form': rating_form, 'beverages': beverages_bar_doesnt_have })

def add_rating(request, bar_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.bar_id = bar_id
    new_rating.save()
  return redirect('bars_detail', bar_id=bar_id)

def assoc_beverage(request, bar_id, beverage_id):
  Bar.objects.get(id=bar_id).beverages.add(beverage_id)
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
  fields = ['name', 'area', 'description']

class BeverageCreate(CreateView):
  model = Beverage
  fields = '__all__'

class BeverageList(ListView):
  model = Beverage

class BeverageDetail(DetailView):
  model = Beverage

class BeverageUpdate(UpdateView):
  model = Beverage
  fields = ['name', 'dankness']

class BeverageDelete(DeleteView):
  model = Beverage
  success_url = '/beverages/'