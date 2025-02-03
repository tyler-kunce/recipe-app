# Recipe App

## About This App
This web application (project) is built using Python's Django framework. This project will feature functions for creating and modifying recipes (name, ingredients, cooking time, and a calculated difficulty). Users will also be able to search for recipes by ingredients.

## Technical Specs
- Django 4.2.16
- SQLite3
- HTML, CSS
- Cloudinary Storage
- Matplotlib

## Models

### Recipes Model
- `name`: `CharField` (max_length = 120)
- `cooking_time`: `FloatField`
- `ingredients`: `TextField`
- `difficulty`: `CharField` (DIFFICULTY_CHOICES = Easy, Medium, Intermediate, Hard)
- `pic`: `CloudinaryField`