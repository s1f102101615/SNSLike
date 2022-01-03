from .models import Article, Comment
from django import forms


class Goto_form(forms.ModelForm):

    class Meta:
        model = goto
        fields = ('image','text')