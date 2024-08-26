from django.urls import path
from . import views

app_name="home"
urlpatterns = [
    path("",views.index,name="index"),
    path("recipes/<int:page_no>",views.recipe_page,name="recipes_view")
]
