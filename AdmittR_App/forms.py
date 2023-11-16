from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from .models import Course, Subject

class AdmissionForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    jamb_score = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(400)]
    )
    waec_aggregate = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    post_utme = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    age = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    first_choice = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")])
    
    
    def clean(self):
        cleaned_data = super().clean()
        course = cleaned_data.get("course")
        subjects = cleaned_data.get("subjects")
        
        if course and subjects:
            # Retrieve the valid subject choices for the selected course from the database
            valid_subjects = course.subject_combo.all().values_list("name", flat=True)
            
            # Check if the selected subjects match the valid subject choices
            selected_subjects = [subject.name for subject in subjects]
            for subject in selected_subjects:
                if subject not in valid_subjects:
                    raise ValidationError(f"{subject} is not a valid subject for {course}")
            
            # Check if the number of selected subjects is not more than 3
            if len(selected_subjects) > 3:
                raise ValidationError("You can select a maximum of 3 subjects")
        
        return cleaned_data
