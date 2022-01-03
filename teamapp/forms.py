from .models import Article
from django import forms

class Goto_form(forms.ModelForm):
    class Meta: 
        model=Article
        fields = ('image','body')
    #class Meta:
        ##fields = ('image','body')