from django.contrib import admin
from .models import AboutMe, EducationEntry, WorkEntry, Skills, Interests

# Register your models here.

admin.site.register(AboutMe)
admin.site.register(EducationEntry)
admin.site.register(WorkEntry)
admin.site.register(Skills)
admin.site.register(Interests)