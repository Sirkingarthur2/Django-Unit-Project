from django import forms
from .models import BlogPost 
 
class AddRecipe(forms.Form): 
    name = forms.CharField() 
    ingredients = forms.Textarea() 
    instructions = forms.Textarea() 
    cook_time = forms.IntegerField(help_text="Enter cook time in minutes")
 
