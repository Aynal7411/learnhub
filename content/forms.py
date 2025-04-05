# content/forms.py
from django import forms
from .models import Tutorial

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 20}),
            'external_links': forms.Textarea(attrs={'rows': 5}),
        }