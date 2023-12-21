from django import forms
from .models import profile,Skill,EducationDetail

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'previous_work': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields=['skill_name']
        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'form-control'}),
            }
