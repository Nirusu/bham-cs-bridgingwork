from django import forms

from .models import AboutMe, EducationEntry, WorkEntry, Skills, Interests


class AboutMeForm(forms.ModelForm):

    class Meta:
        model = AboutMe
        fields = ('name', 'dob', 'email', 'name', 'text')

class EducationEntryForm(forms.ModelForm):

    class Meta:
        model = EducationEntry
        fields = ('title', 'fromDate', 'fromDateShown', 'toDate', 'toDateShown', 'company', 'text')

    
class WorkEntryForm(forms.ModelForm):

    class Meta:
        model = WorkEntry
        fields = ('title', 'fromDate', 'fromDateShown', 'toDate', 'toDateShown', 'company', 'text')


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('skills',)

class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ('interests',)