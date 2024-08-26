from django.shortcuts import render
from django.core.paginator import Paginator

from recipe.models import Recipe

# Create your views here.
def index(request):
    return render(request,"home/index.html")


def recipe_page(request,page_no):
    recipes=Recipe.objects.all().order_by("recipe_name")
    paginator=Paginator(recipes,10)
    
    page_recipes=paginator.get_page(page_no)
    context={
        "recipes":page_recipes
    }
    print(page_recipes)
    return render(request,"home/recipes.html",context)