from django import forms
from .models import Tag

class SearchForm(forms.Form):
    '''tag_options = Tag.objects.all()
    OPTIONS = []
    for option in tag_options
        OPTIONS.append(option.title)'''
    tagfield = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())
