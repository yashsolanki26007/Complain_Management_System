from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['student_name', 'enrollment_no', 'department', 'category', 'description']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'enrollment_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter enrollment number'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your complaint...'}),
        }

    def clean_student_name(self):
        name = self.cleaned_data.get('student_name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name

    def clean_enrollment_no(self):
        enroll = self.cleaned_data.get('enrollment_no')
        if len(enroll) < 5:
            raise forms.ValidationError("Enter a valid enrollment number.")
        return enroll