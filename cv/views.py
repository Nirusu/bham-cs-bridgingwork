from django.shortcuts import render
from .models import AboutMe, EducationEntry, WorkEntry, Skills, Interests

# Create your views here.

def cv_show(request):
    try:
        aboutme = AboutMe.objects.latest('id')
    except AboutMe.DoesNotExist:
        aboutme = None

    education = EducationEntry.objects.order_by('-toDate')
    work = WorkEntry.objects.order_by('-toDate')

    try:
        skills = Skills.objects.latest('id')
    except Skills.DoesNotExist:
        skills = None
    
    try:
        interests = Interests.objects.latest('id')
    except Interests.DoesNotExist:
        interests = None

    return render(request, 'cv/cv_show.html', {'aboutme':aboutme, 'education':education, 'work':work, 'skills':skills, 'interests':interests})