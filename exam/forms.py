from django import forms
from django.forms import ModelForm
from .models import exam_details

class ExamCreationForm(forms.ModelForm):
    class Meta:
        model = exam_details
        fields = ['name', 'questions']
        
    def __init__(self, *args, **kwargs):
        super(ExamCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
