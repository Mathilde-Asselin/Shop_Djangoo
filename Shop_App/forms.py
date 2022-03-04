from django import forms
from .models import Card
 
 
# creating a form
class CardForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Card
 
        # specify fields to be used
        fields = [
            "title",
            "img",
            "description",
            "price",
            "quantity",
        ]

class UpdateForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Card 
 
        # specify fields to be used
        fields = [
            "quantity",
        ]