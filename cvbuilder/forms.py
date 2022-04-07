from .models import Experience, Resume
from django import forms
from .widgets import CustomClearableFileInput
# from ckeditor.widgets import CKEditorWidget


class ResumeForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=CustomClearableFileInput())

    class Meta:
        model = Resume
        fields = ['image', 'name', 'email', 'telephone', 'linkedin', 'github',
                  'website', 'description', 'career_summary', 'template']
       


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'duration', 'text', 'tech']
        