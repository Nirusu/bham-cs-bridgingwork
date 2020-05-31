from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_show, name='cv_show'),
    path('aboutme/new/', views.aboutme_new, name='aboutme_new'),
    path('aboutme/<int:pk>/edit/', views.aboutme_edit, name='aboutme_edit'),
    path('aboutme/<int:pk>/remove/', views.aboutme_remove, name='aboutme_remove'),
    path('education/new/', views.education_new, name='education_new'),
    path('education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('education/<int:pk>/remove/', views.education_remove, name='education_remove'),
    path('work/new/', views.work_new, name='work_new'),
    path('work/<int:pk>/edit/', views.work_edit, name='work_edit'),
    path('work/<int:pk>/remove/', views.work_remove, name='work_remove'),
    path('skills/new/', views.skills_new, name='skills_new'),
    path('skills/<int:pk>/edit/', views.skills_edit, name='skills_edit'),
    path('skills/<int:pk>/remove/', views.skills_remove, name='skills_remove'),
    path('interests/new/', views.interests_new, name='interests_new'),
    path('interests/<int:pk>/edit/', views.interests_edit, name='interests_edit'),
    path('interests/<int:pk>/remove/', views.interests_remove, name='interests_remove'),
]