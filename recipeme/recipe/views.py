from django.shortcuts import render,redirect,get_object_or_404

from chef.models import Chef
from .models import Recipe

from .forms import CreateRecipeForm

from django.contrib.auth.decorators import login_required

@login_required
def create(request):  
    #when user submits the data
    if request.method=="POST":
        formdata=CreateRecipeForm(request.POST)
        
        if formdata.is_valid() and request.user.is_authenticated:
            #getting fields
            name=formdata.cleaned_data["name"]
            difficulty=formdata.cleaned_data["difficulty"]
            instructions=formdata.cleaned_data["instructions"]
            description=formdata.cleaned_data["description"]

            chef=Chef.objects.get(username=request.user.username)

            recipe = Recipe(recipe_name=name,difficulty=difficulty,created_by=chef,instructions=instructions,description=description)
            recipe.save()

            return redirect("chef:account")
    
    form=CreateRecipeForm()
    context={
        "form":form
    }
    return render(request,"recipe/create.html",context)


@login_required
def detail_recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe,pk=recipe_id)
    editable=recipe.created_by.username == request.user.username
    context={
        "editable":editable,
        "recipe":recipe
    }
    return render(request,"recipe/details.html",context)

@login_required
def edit(request,recipe_id):  

    recipe=get_object_or_404(Recipe,pk=recipe_id)

    if request.method=="POST":
        formdata=CreateRecipeForm(request.POST)
        
        if formdata.is_valid() and request.user.is_authenticated:
            #getting fields
            name=formdata.cleaned_data["name"]
            difficulty=formdata.cleaned_data["difficulty"]
            instructions=formdata.cleaned_data["instructions"]
            description=formdata.cleaned_data["description"]
            
            recipe.recipe_name=name
            recipe.description=description
            recipe.difficulty=difficulty
            recipe.instructions=instructions
            
            recipe.save()

            return redirect("chef:account")
        
    form=CreateRecipeForm(initial={
            'name': recipe.recipe_name,
            'difficulty': recipe.difficulty,
            'instructions': recipe.instructions,
            'description': recipe.description,
    })
    context={
        "form":form,
        "recipe":recipe
    }
    return render(request,"recipe/edit.html",context)


@login_required
def delete(request,recipe_id):
    recipe=get_object_or_404(Recipe,pk=recipe_id)
    recipe.delete()
    return redirect("chef:account")