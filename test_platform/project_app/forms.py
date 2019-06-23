from django import forms
from project_app.models import Project


class ProjectForms(forms.ModelForm):
    # name = forms.CharField(label='ProjectName', max_length=100)
    # describe = forms.CharField(label='Description', widget=forms.Textarea)
    # status = forms.BooleanField(label="Status", required=True)

    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
