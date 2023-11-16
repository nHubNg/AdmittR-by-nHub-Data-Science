from django.shortcuts import render
from .forms import AdmissionForm
from .prediction import predict


# Create your views here.
def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            subjects = [subject.name for subject in form.cleaned_data['subjects']]
            data = {
                'COURSE': [form.cleaned_data['course'].name],
                'Jamb_Score': [form.cleaned_data['jamb_score']],
                'Waec_Agg': [form.cleaned_data['waec_aggregate']],
                'Post_Utme': [form.cleaned_data['post_utme']],
                'Age': [form.cleaned_data['age']],
                'FirstChoice': [form.cleaned_data['first_choice']],
                'Subject_Combo': str(subjects),
            }
            
            data_copy = {
                'Course': [form.cleaned_data['course'].name],
                'Jamb_Score': [form.cleaned_data['jamb_score']],
                'Waec_Agg': [form.cleaned_data['waec_aggregate']],
                'Post_Utme': [form.cleaned_data['post_utme']],
                'Age': [form.cleaned_data['age']],
                'First_Choice': [form.cleaned_data['first_choice']],
                'Subject_Combo': subjects,
            }
            
            admission_results = predict(data_copy)
            
            return render(request, 'result.html', {'data': data, 'admission_results' : admission_results, 'data_copy': data_copy})
    else:
        form = AdmissionForm()
    
    return render(request, 'admission_form.html', {'form': form})
