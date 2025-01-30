from django import forms
from .models import Recipe

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
    )

# define class-based Form imported from Django forms
class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cooking_time', 'ingredients', 'pic']