from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project

def home(request):
    return render(request, "home.html")

login_required
def dashboard(request):
    projects = Project.objects.filter(created_by=request.user)

    return render(request, "dashboard.html", {
        "projects": projects
    })

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect("dashboard")   # Project banne ke baad Dashboard par jayega
    else:
        form = ProjectForm()

    return render(request, "create_project.html", {"form": form})