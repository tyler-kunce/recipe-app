from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time', 'ingredients', 'image_preview')
    search_fields = ('name',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.pic:
            return f'<img src="{obj.pic.url}" width="100" height="100" />'
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)