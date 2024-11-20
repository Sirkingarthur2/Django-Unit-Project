from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'home.html')


def blog_view(request):


    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})


def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        cook_time = request.POST.get('cook_time')

        new_recipe = RecommendRecipe(name=name, ingredients=ingredients, instructions=instructions, cook_time=cook_time)
        new_recipe.save()

        return redirect('recipes')

    return render(request, 'add_recipe.html')


def recipe_view(request):
    recipes = Recipes.objects.all()
    
    return render(request, 'recipes.html', {'recipes': recipes})


