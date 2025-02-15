from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Recipe
from .forms import RecipesSearchForm, RecipesForm
from .utils import get_chart, get_recipename_from_id

import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

def about_me(request):
    return render(request, 'recipes/about_me.html')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)
        print("Form is valid")
        if form.is_valid():
            try:
                form.save()
                print("Form saved successfully")
                return redirect('recipes:list')
            except Exception as e:
                print("Error saving form:", e)
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)
    else:
        form = RecipesForm()
    return render(request, 'recipes/recipes_add.html', {'form': form})

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe

    def get(self, request):
        form = RecipesSearchForm()
        recipes = Recipe.objects.all()

        context = {
            'form': form,
            'recipes': recipes,
        }

        return render(request, 'recipes/recipes_list.html', context)
    
    def post(self, request):
        form = RecipesSearchForm(request.POST)
        recipes = Recipe.objects.all()
        chart = None

        if form.is_valid():
            # import pdb; pdb.set_trace()
            recipe_name = form.cleaned_data.get('recipe_name')
            chart_type = form.cleaned_data.get('chart_type')

            qs = Recipe.objects.filter(Q(name__icontains=recipe_name) | Q(ingredients__icontains=recipe_name))
            if qs.exists():
                recipes = pd.DataFrame(qs.values())
                recipes['id'] = recipes['id'].apply(get_recipename_from_id)
                chart = get_chart(chart_type, recipes, labels = recipes['id'].values)
                recipes = qs

        context = {
            'form': form,
            'recipes': recipes,
            'chart': chart,
        }

        return render(request, 'recipes/recipes_list.html', context)
    

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'