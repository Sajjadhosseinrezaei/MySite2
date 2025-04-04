from django.shortcuts import render
from django.views import View
from .models import Project, Skill

# Create your views here.


class ProjectAndSkillListView(View):

    def get(self, request):
        context = {
            'projects': Project.objects.all(),
            'skills': Skill.objects.all(),
        }
        return render(request, 'home/home.html', context)
    