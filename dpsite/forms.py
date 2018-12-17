from django import forms
from .models import Tag

class SearchForm(forms.Form):
    tagfield = forms.ModelMultipleChoiceField(label = "Tags", required = False, widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())
