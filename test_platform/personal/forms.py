from django import forms
from personal.models import Project
from personal.models import Module


class ProjectForms(forms.ModelForm):
    # name = forms.CharField(label='ProjectName', max_length=100)
    # describe = forms.CharField(label='Description', widget=forms.Textarea)
    # status = forms.BooleanField(label="Status", required=True)

    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']


class ModuleForms(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'describe', 'project']
