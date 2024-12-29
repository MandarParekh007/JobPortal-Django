from django import forms
from .models import Company, Job,Tag

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name','description']


class JobForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Enter tags separated by commas'}),
        label="Tags"
    )   
    class Meta:
        model = Job
        fields = ['title', 'description','salary','tags']
