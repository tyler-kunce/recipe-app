from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time', 'ingredients')
    search_fields = ('name',)
    readonly_fields = ('pic',)

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)