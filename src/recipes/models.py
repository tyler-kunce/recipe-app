from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard')
    ]

    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='(in minutes)')
    ingredients = models.TextField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    def return_ingredients_as_list(self):
        return self.ingredients.split(', ')
        
    def calculate_difficulty(self):
        ingredient_len = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and ingredient_len < 4:
            return "Easy"
        elif self.cooking_time < 10 and ingredient_len >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and ingredient_len < 4:
            return "Intermediate"
        elif self.cooking_time >= 10 and ingredient_len >= 4:
            return "Hard"
    
    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)