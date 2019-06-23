from django import forms
from module_app.models import Module


class ModuleForms(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'describe', 'project']
