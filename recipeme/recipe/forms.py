from django import forms

class CreateRecipeForm(forms.Form):
    name=forms.CharField(max_length=100,label="Name")
    difficulty=forms.ChoiceField(choices=[("easy","Easy"),("medium","Medium"),("Hard","hard")])
    instructions=forms.CharField(widget=forms.Textarea)
    description=forms.CharField(widget=forms.Textarea)