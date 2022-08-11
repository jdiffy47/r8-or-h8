from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bar
from .forms import RatingForm
# from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def bars_index(request):
  bars = Bar.objects.all()
  return render(request, 'bars/index.html', { 'bars': bars })

@login_required
def bars_detail(request, bar_id):
  bar = Bar.objects.get(id=bar_id)
  # beverages_bar_doesnt_have = Beverage.objects.exclude(id__in = bar.beverages.all().values_list('id'))
  rating_form = RatingForm()
  return render(request, 'bars/detail.html', { 'bar': bar, 'rating_form': rating_form })

def add_rating(request, bar_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.bar_id = bar_id
    new_rating.save()
  return redirect('bars_detail', bar_id=bar_id)

@login_required
def assoc_beverage(request, bar_id, beverage_id):
  Bar.objects.get(id=bar_id).beverages.add(beverage_id)
  return redirect('bars_detail', bar_id=bar_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('bars_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class BarCreate(LoginRequiredMixin, CreateView):
  model = Bar
  fields = ['name', 'area', 'description']
  success_url = '/bars/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BarUpdate(LoginRequiredMixin, UpdateView):
  model = Bar
  fields = ['name', 'area', 'description']

class BarDelete(LoginRequiredMixin, DeleteView):
  model = Bar
  success_url = '/bars/'
  fields = ['name', 'area', 'description']

# class BeverageCreate(LoginRequiredMixin, CreateView):
#   model = Beverage
#   fields = '__all__'

# class BeverageList(LoginRequiredMixin, ListView):
#   model = Beverage

# class BeverageDetail(LoginRequiredMixin, DetailView):
#   model = Beverage

# class BeverageUpdate(LoginRequiredMixin, UpdateView):
#   model = Beverage
#   fields = ['name', 'dankness']

# class BeverageDelete(LoginRequiredMixin, DeleteView):
#   model = Beverage
#   success_url = '/beverages/'