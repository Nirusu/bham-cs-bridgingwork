from django.shortcuts import render
from .models import AboutMe, EducationEntry, WorkEntry, Skills, Interests

# Create your views here.

def cv_show(request):
    aboutme = AboutMe.objects.latest('id')
    education = EducationEntry.objects.all()
    work = WorkEntry.objects.all()
    skills = Skills.objects.latest('id')
    interests = Interests.objects.latest('id')
    return render(request, 'cv/cv_show.html', {'aboutme':aboutme, 'education':education, 'work':work, 'skills':skills, 'interests':interests})