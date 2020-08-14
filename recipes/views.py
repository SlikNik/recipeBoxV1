from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from recipes.models import Author, Recipe
from recipes.forms import SignupForm, LoginForm, AddAuthorForm, AddRecipeForm

in_out = 'login'
# Create your views here.

def index_view(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': all_recipes, 'in_out': in_out})

def author_detail_view(request, author_name):
    current_author = Author.objects.filter(name=author_name).first()
    author_recipes = Recipe.objects.filter(author=current_author)
    return render(request, 'author_detail.html', {'author': current_author, 'recipes': author_recipes})

def recipe_detail_view(request, recipe_id):
    current_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': current_recipe})

@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('homepage'))
        form = AddAuthorForm()
        return render(request, 'generic_form.html', {'form': form})
    else:
        return render(request, 'no_access.html', {'user': request.user})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            if request.user.is_staff:
                form.save()
                return HttpResponseRedirect(reverse('homepage'))
            else:
                form.check_user(request)
                form.save()
                return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()
    return render(request, 'add_recipe_form.html',  {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('firstname').lower() + data.get('lastname').lower()
            new_user = User.objects.create_user(username=username, password=data.get('password'))
            Author.objects.create(name=data.get('firstname').capitalize() + ' ' + data.get('lastname').capitalize(), bio=data.get('bio'), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html',  {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse('homepage'))
                return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
      
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

                