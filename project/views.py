from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import ProjectForm
from .models import Project



def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user:

            login(request, user)

            return redirect("dashboard")


        else:

            messages.error(
                request,
                "Invalid username or password"
            )


    return render(
        request,
        "login.html"
    )





def register_view(request):


    if request.method == "POST":


        username = request.POST.get("username")

        password = request.POST.get("password")



        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )


        else:


            User.objects.create_user(

                username=username,

                password=password

            )


            messages.success(
                request,
                "Account created successfully"
            )


            return redirect(
                "login"
            )



    return render(
        request,
        "register.html"
    )







@login_required
def dashboard(request):


    projects = Project.objects.filter(
        created_by=request.user
    )



    context = {


        "projects": projects,


        "total_projects": projects.count(),



        "completed_projects": projects.filter(
            status="Completed"
        ).count(),



        "progress_projects": projects.filter(
            status="Progress"
        ).count(),



        "pending_projects": projects.filter(
            status="Planning"
        ).count(),


    }



    return render(
        request,
        "dashboard.html",
        context
    )


@login_required
def create_project(request):

    if request.method == "POST":

        print("POST DATA:", request.POST)

        form = ProjectForm(request.POST)


        if form.is_valid():

            print("FORM VALID")

            project = form.save(commit=False)

            project.created_by = request.user

            project.save()

            print("PROJECT SAVED")

            return redirect("dashboard")


        else:

            print("FORM ERROR:", form.errors)


    else:

        form = ProjectForm()


    return render(
        request,
        "create_project.html",
        {
            "form": form
        }
    )










@login_required
def delete_project(request, id):


    project = get_object_or_404(

        Project,

        id=id,

        created_by=request.user

    )


    project.delete()



    messages.success(
        request,
        "Project deleted"
    )


    return redirect(
        "dashboard"
    )







def logout_view(request):


    logout(request)


    return redirect(
        "login"
    )