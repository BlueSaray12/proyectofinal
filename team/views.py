from django.shortcuts import render
from .models import Project
# Create your views here.
def team(request):
    projects=Project.objects.all()
    return render(request, "team/team.html", {'listProjects':projects})

