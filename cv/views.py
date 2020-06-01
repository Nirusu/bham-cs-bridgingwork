from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import AboutMe, EducationEntry, WorkEntry, Skills, Interests
from .forms import AboutMeForm, EducationEntryForm, WorkEntryForm, SkillsForm, InterestsForm

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

@login_required
def aboutme_new(request):
    if request.method == "POST":
        form = AboutMeForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = AboutMeForm()
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def aboutme_edit(request, pk):
    post = get_object_or_404(AboutMe, pk=pk)
    if request.method == "POST":
        form = AboutMeForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = AboutMeForm(instance=post)
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def aboutme_remove(request, pk):
    entry = get_object_or_404(AboutMe, pk=pk)
    entry.delete()
    return redirect('/cv')

@login_required
def education_new(request):
    if request.method == "POST":
        form = EducationEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = EducationEntryForm()
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def education_edit(request, pk):
    post = get_object_or_404(EducationEntry, pk=pk)
    if request.method == "POST":
        form = EducationEntryForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = EducationEntryForm(instance=post)
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def education_remove(request, pk):
    entry = get_object_or_404(EducationEntry, pk=pk)
    entry.delete()
    return redirect('/cv')

@login_required
def work_new(request):
    if request.method == "POST":
        form = WorkEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = WorkEntryForm()
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def work_edit(request, pk):
    post = get_object_or_404(WorkEntry, pk=pk)
    if request.method == "POST":
        form = WorkEntryForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = WorkEntryForm(instance=post)
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def work_remove(request, pk):
    entry = get_object_or_404(WorkEntry, pk=pk)
    entry.delete()
    return redirect('/cv')


@login_required
def skills_new(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = SkillsForm()
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def skills_edit(request, pk):
    post = get_object_or_404(Skills, pk=pk)
    if request.method == "POST":
        form = SkillsForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = SkillsForm(instance=post)
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def skills_remove(request, pk):
    entry = get_object_or_404(Skills, pk=pk)
    entry.delete()
    return redirect('/cv')


@login_required
def interests_new(request):
    if request.method == "POST":
        form = InterestsForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = InterestsForm()
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def interests_edit(request, pk):
    post = get_object_or_404(Interests, pk=pk)
    if request.method == "POST":
        form = InterestsForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('/cv')
    else:
        form = InterestsForm(instance=post)
    return render(request, 'cv/entry_edit.html', {'form': form})

@login_required
def interests_remove(request, pk):
    entry = get_object_or_404(Interests, pk=pk)
    entry.delete()
    return redirect('/cv')