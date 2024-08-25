from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import CreateRecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def create(request):  
    #when user submits the data
    if request.method=="POST":
        formdata=CreateRecipeForm(request.POST)
        
        if formdata.is_valid() and request.user.is_authenticated():
            #getting fields
            name=formdata.cleaned_data["name"]
            difficulty=formdata.cleaned_data["difficulty"]

            recipe = Recipe(recipe_name=name,difficulty=difficulty)
            recipe.save()
            return redirect("/recipe")
    
    form=CreateRecipeForm()
    context={
        "form":form
    }
    return render(request,"recipe/create.html",context)