from django.db import models
from chef.models import Chef

# Create your models here.
class Recipe(models.Model):

    def __str__(self):
        return self.recipe_name+self.created_by.first_name
    
    DIFFICULTY_LEVELS=[("easy","Easy"),("medium","Medium"),("Hard","hard")]

    recipe_name=models.CharField(max_length=100)
    created_by=models.ForeignKey(Chef,on_delete=models.CASCADE)
    difficulty=models.CharField(choices=DIFFICULTY_LEVELS,max_length=10,default="easy")
    