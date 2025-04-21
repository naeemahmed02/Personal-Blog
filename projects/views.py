from django.shortcuts import render
from projects.models import Project

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'projects.html', context)


def project_detail(request, project_slug):
    # Get single project
    project = Project.objects.get(slug = project_slug)
    context = {'project': project}
    return render(request, 'project_detail_page.html', context)