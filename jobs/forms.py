from django import forms
from .models import Company, Job

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name','description']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']  # Explicitly specify fields
