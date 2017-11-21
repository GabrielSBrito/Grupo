from django.contrib import admin

from core.models import Curso,Aluno,Matricula

from django.contrib.auth.admin import UserAdmin
from django import forms

# Register your models here.

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso','celular')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'
        if commit:
            user.save()

        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email', 'nome', 'curso','celular')
        
class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm


class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('email', 'nome', 'curso','celular')}),)
    add_fieldsets = (
        (None, {
            'fields': ('ra', 'email', 'nome', 'curso','celular')

            } ),
             
         )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()




class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo','carga_horaria')
    list_filter = ('tipo',)

admin.site.register(Curso,      CursoAdmin)
admin.site.register(Aluno,      AlunoAdmin)
admin.site.register(Matricula)