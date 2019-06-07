from django import forms
from personal.models.project import Project

class ProjectForm(forms.ModelForm):
    # name = forms.CharField(label='名称', max_length=50)
    # describe = forms.CharField(label='描述', widget=forms.Textarea)
    # status = forms.BooleanField(label='状态', required=True)

    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
