# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    ra = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    sigla_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='sigla_curso')

    class Meta:
        managed = False
        db_table = 'aluno'


class Arquivosquestao(models.Model):
    nome_disciplina = models.ForeignKey('Questao', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao')
    arquivo = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'arquivosquestao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'arquivo'),)


class Arquivosresposta(models.Model):
    nome_disciplina = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='numero_questao')
    ra_aluno = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='ra_aluno')
    arquivo = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'arquivosresposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno', 'arquivo'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Curso(models.Model):
    sigla = models.CharField(primary_key=True, max_length=5)
    nome = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'curso'


class Cursoturma(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    nome_disciplina = models.ForeignKey('Turma', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'cursoturma'
        unique_together = (('sigla_curso', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Disciplina(models.Model):
    nome = models.CharField(primary_key=True, max_length=240)
    carga_horaria = models.IntegerField()
    teoria = models.DecimalField(max_digits=3, decimal_places=0)
    pratica = models.DecimalField(max_digits=3, decimal_places=0)
    ementa = models.TextField(blank=True, null=True)
    competencias = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)
    bibliografia_basica = models.TextField(blank=True, null=True)
    bibliografia_complementar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'


class Disciplinaofertada(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'disciplinaofertada'
        unique_together = (('nome_disciplina', 'ano', 'semestre'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gradecurricular(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'gradecurricular'
        unique_together = (('sigla_curso', 'ano', 'semestre'),)


class Matricula(models.Model):
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ra_aluno', primary_key=True)
    nome_disciplina = models.ForeignKey('Turma', models.DO_NOTHING, db_column='nome_disciplina')
    ano_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    ano_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='ano_grade')
    semestre_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='semestre_grade')
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero'),)


class Periododisciplina(models.Model):
    sigla_curso = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    ano_grade = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='ano_grade')
    semestre_grade = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='semestre_grade')
    numero_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='numero_periodo')
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='nome_disciplina')

    class Meta:
        managed = False
        db_table = 'periododisciplina'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero_periodo', 'nome_disciplina'),)


class Professor(models.Model):
    ra = models.IntegerField(primary_key=True)
    apelido = models.CharField(unique=True, max_length=30, blank=True, null=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'


class Questao(models.Model):
    nome_disciplina = models.ForeignKey('Turma', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero = models.IntegerField()
    data_limite_entrega = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero'),)


class Resposta(models.Model):
    nome_disciplina = models.ForeignKey(Questao, models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey(Questao, models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey(Questao, models.DO_NOTHING, db_column='semestre_ofertado')
    id_turma = models.ForeignKey(Questao, models.DO_NOTHING, db_column='id_turma')
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='numero_questao')
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='ra_aluno')
    data_avaliacao = models.DateField(blank=True, null=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    avaliacao = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_de_envio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno'),)


class Turma(models.Model):
    nome_disciplina = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='ano_ofertado')
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='semestre_ofertado')
    id = models.CharField(max_length=1)
    turno = models.CharField(max_length=5)
    ra_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ra_professor')

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id'),)
