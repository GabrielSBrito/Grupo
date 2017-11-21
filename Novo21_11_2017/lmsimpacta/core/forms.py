from django import forms
from core.models import Curso
from django import forms
from django.contrib.auth.models import User

from core.models import Curso,Aluno, Matricula

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = "__all__"