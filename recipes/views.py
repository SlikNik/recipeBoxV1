from django.shortcuts import render
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

def add_author_view(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bio = form.cleaned_data['bio']
            print(name, bio)
            form.save()
    form = AddAuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_recipe_view(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            time_required = form.cleaned_data['time_required']
            instructions = form.cleaned_data['instructions']
            print(title, author, description, time_required, instructions)
            form.save()
    form = AddRecipeForm()
    return render(request, 'add_recipe.html',  {'form': form})
    