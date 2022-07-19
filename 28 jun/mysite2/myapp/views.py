from django.shortcuts import render
from .models import*
from .forms import*
# Create your views here.
def form(request):
    fm = CandidateForm()
    fm2 = JobForm()
    fm3 = ApplicationForm()
    fm4 = QualificationForm()
    fm5 = InterviewUpdateForm()
    return render(request, 'form.html', {'form':fm,'form2':fm2,'form3':fm3,'form4':fm4,'form5':fm5})
            