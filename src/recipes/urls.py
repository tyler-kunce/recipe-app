from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, about_me, add_recipe

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home-url'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('about/', about_me, name='about_me'),
    path('add/', add_recipe, name='add'),
]