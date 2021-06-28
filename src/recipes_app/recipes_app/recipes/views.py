from django.shortcuts import render, redirect

from recipes_app.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes_app.recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    # else:
    form = DeleteRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form
    }

    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if recipe:
        context = {
            'recipe': recipe,
            'ingredients': recipe.ingredients.split(', ')
        }

        return render(request, 'details.html', context)
