from django.urls import path
from . import views

app_name = 'recipe'
urlpatterns=[
    path("create/",views.create,name="create"),
    path("edit/<int:recipe_id>",views.edit,name="edit"),
    path("delete/<int:recipe_id>",views.delete,name="delete"),
    path("get/<int:recipe_id>",views.detail_recipe,name="detail_recipe"),
]