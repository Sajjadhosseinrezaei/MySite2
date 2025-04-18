from django.db import models

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    name = models.CharField(max_length=80)
    technologies = models.ManyToManyField(Technology,
                                           blank=True,
                                             related_name='projects')
    description = models.TextField()
    github = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=80)
    icon = models.URLField(blank=True, null=True)
    skill_level = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
