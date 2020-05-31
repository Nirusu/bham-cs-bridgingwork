from django.shortcuts import render

# Create your views here.

def cv_show(request):
    return render(request, 'cv/cv_show.html')