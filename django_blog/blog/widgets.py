# blog/widgets.py
from django import forms

class TagWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
