from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.login_view,
        name="login"
    ),

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "create-project/",
        views.create_project,
        name="create_project"
    ),

    path(
        "delete-project/<int:id>/",
        views.delete_project,
        name="delete_project"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

]