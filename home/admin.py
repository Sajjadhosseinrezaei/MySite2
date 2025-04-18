from django.contrib import admin
from .models import Technology, Project, Skill
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'description', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')
    ordering = ('-created',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'skill_level', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')
    ordering = ('-created',)




admin.site.unregister(Group)