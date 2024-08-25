from django.shortcuts import render,redirect

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

            chef=Chef.objects.get(username=request.user.username)

            recipe = Recipe(recipe_name=name,difficulty=difficulty,created_by=chef)
            recipe.save()

            return redirect("chef:account")
    
    form=CreateRecipeForm()
    context={
        "form":form
    }
    return render(request,"recipe/create.html",context)