from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from recipes.models import Author, Recipe
from recipes.forms import AddAuthorForm, AddRecipeForm

# Create your views here.

def index_view(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': all_recipes})

def author_detail_view(request, author_name):
    current_author = Author.objects.filter(name=author_name).first()
    author_recipes = Recipe.objects.filter(author=current_author)
    return render(request, 'author_detail.html', {'author': current_author, 'recipes': author_recipes})

def recipe_detail_view(request, recipe_id):
    current_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': current_recipe})

def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpRepsonseRedirect(reverse('author_view'))

    form = AddAuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpRepsonseRedirect(reverse('recipe_view'))

    form = AddRecipeForm()
    return render(request, 'add_recipe.html',  {'form': form})
    