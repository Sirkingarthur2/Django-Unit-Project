from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Recipes)
admin.site.register(BlogPost)
admin.site.register(RecommendRecipe)