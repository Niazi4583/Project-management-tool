from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:

        model = Project


        fields = [
            "name",
            "description",
            "status",
            "progress",
            "color",
        ]


        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder":"Project name"
                }
            ),


            "description": forms.Textarea(
                attrs={
                    "placeholder":"Project description"
                }
            ),


            "progress": forms.NumberInput(
                attrs={
                    "min":0,
                    "max":100
                }
            ),


            "color": forms.TextInput(
                attrs={
                    "type":"color"
                }
            ),

        }