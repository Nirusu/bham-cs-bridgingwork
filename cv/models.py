from django.db import models

class AboutMe(models.Model):
    # No phone numbers or similar, it's public after all
    name = models.CharField(max_length = 50)
    dob = models.DateField()
    email = models.EmailField()
    name = models.CharField(max_length = 100)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text

class EducationEntry(models.Model):
    title = models.CharField(max_length=200)
    fromYear = models.CharField(max_length=50) # Don't want a full-flegded DateField for an abbreviated date
    toYear = models.CharField(max_length=20) # Don't want a full-flegded DateField for an abbreviated date
    company = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class WorkEntry(models.Model):
    title = models.CharField(max_length=200)
    fromYear = models.CharField(max_length=50)
    toYear = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Skills(models.Model):
    skills = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.skills

class Interests(models.Model):
    interests = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.interests