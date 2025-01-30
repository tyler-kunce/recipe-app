from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe
from .forms import RecipesSearchForm

# Create your tests here.
class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            username='tester',
            password='testing'
        )

        # Set up non-modified objects used by all test methods
        cls.test_recipe = Recipe.objects.create(
            name = 'Coffee',
            ingredients = 'Coffee grounds, Water, Sugar, Milk',
            cooking_time = 5,
        )
    
    def setUp(self):
        self.client = Client()
    
    def test_recipe_name(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')
    
    def test_recipe_name_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        max_length = recipe._meta.get_field('name').max_length

        # Compare the value to the expected result
        self.assertEqual(max_length, 120)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        # get_absolute_url() should take you to the detail page of recipe #1
        # and load the URL /recipes/list/1
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_add_recipe(self):
        self.client.login(username='tester', password='testing')
        response = self.client.post(reverse('recipes:add'), {
            'name': 'Coffee',
            'ingredients': 'Coffee grounds, Water, Sugar, Milk',
            'cooking_time': 5,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Recipe.objects.filter(name='Coffee').exists())

class RecipeSearchFormTest(TestCase):
    def test_search_recipe_valid(self):
        form_data = {
            'recipe_name': 'coffee',
            'chart_type': '#1'
        }
        form = RecipesSearchForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_search_ingredient_valid(self):
        form_data = {
            'recipe_name': 'water',
            'chart_type': '#1'
        }
        form = RecipesSearchForm(data = form_data)
        self.assertTrue(form.is_valid())