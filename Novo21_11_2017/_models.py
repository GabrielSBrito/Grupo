class Disciplina(models.Model):
    nome = models.CharField(max_length=240)
    carga_horaria = models.SmallIntegerField()  #tinyint
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()

    def __str__(self):
        return "{}: {} - {}".format(self.nome, self.carga_horaria, self.teoria)

    class Meta:
        db_table = 'Disciplina'

class Professor(models.Model):
    ra = models.IntegerField(unique = True, null = False)
    apelido = models.CharField(max_length=30,unique = True, null = True)
    nome = models.CharField(max_length =  120)
    email = models.CharField(max_length =  80)
    celular = models.CharField(max_length =  11)

    def __str__(self):
        return "{} - {}".format(self.ra, self.apelido)

    class Meta:
        db_table = 'Professor'

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(to='Disciplina', related_name="disciplinasOfertadas", null=False, blank=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    def __str__(self):
        return "{}: {} - {}".format(self.disciplina, self.ano, self.semestre)
    class Meta:
        db_table = 'DisciplinaOfertada'

class Curso(models.Model):
    #alunos = models.ManyToOneField(to='Aluno')
    sigla = models.CharField(max_length=5,unique=True,null=False)
    nome = models.CharField(max_length=50,unique=True,null=False)
    #turmas = models.ManyToManyField(Turma, db_table='CursoTurma', related_name='cursos', blank=False)

    def __str__(self):
        return "{} - {}".format(self.sigla,self.nome)

    class Meta:
        db_table = 'Curso'

class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', related_name="gradesCurriculares", null=False, blank=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)
    
    def __str__(self):
        return "{}: {} - {}".format(self.curso, self.ano, self.semestre)
    class Meta:
        db_table = 'GradeCurricular'

class Periodo(models.Model):
    gradeCurricular = models.ForeignKey(to='GradeCurricular', related_name="periodos", null=False, blank=False) #onetomany
    numero = models.SmallIntegerField(null=False) #tinyint
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return "{}: {} - {}".format(self.numero)

    class Meta:
        db_table = 'Periodo'

class Turma(models.Model):
    disciplinaOfertada = models.ForeignKey(to='DisciplinaOfertada', related_name="turmas", null=False, blank=False) #onetomany
    professor = models.ForeignKey(to='Professor', related_name="turmas", null=False, blank=False) #onetomany
    turno = models.CharField(max_length=15)
    turma_sigla = models.CharField(max_length=1)
    cursos = models.ManyToManyField('Curso', db_table='CursoTurma', related_name='turmas', blank=False)

    def __str__(self):
        return "{} - {}".format(self.turma_sigla, self.turno)

    class Meta:
        db_table = 'Turma'

class Questao(models.Model):
    turma = models.ForeignKey(to='Turma', related_name="questoes", null=False, blank=False) #onetomany
    descricao = models.TextField()
    data_limite_entrega = models.DateField()
    numero = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return "{} - {}: {}".format(self.turma.turma_sigla, self.id, self.descricao)

    class Meta:
        db_table = 'Questao'

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(to='Questao', related_name="arquivosQuestao", null=False, blank=False) #onetomany
    arquivo = models.CharField(max_length=500)

    def __str__(self):
        return "{}: {}".format(self.questao, self.id)
    class Meta:
        db_table = 'ArquivosQuestao'

class Aluno(models.Model):
    curso = models.ForeignKey(to='Curso', related_name="alunos", null=False, blank=False) #onetomany
    nome = models.CharField(max_length=120,null=False)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)
    ra = models.IntegerField(unique=True,null=False)
    turmas = models.ManyToManyField('Turma', db_table='Matricula', related_name='alunos', blank=True)
    foto = models.ForeignKey(to='ArquivosFoto', related_name="alunos", null=True, blank=True) #onetomany

    def __str__(self):
        return "{} - {}".format(self.ra,self.nome)
    
    class Meta:
        db_table = 'Aluno'

class Resposta(models.Model):
    aluno = models.ForeignKey(to='Aluno', related_name="respostas", null=False, blank=False) #onetomany
    questao = models.ForeignKey(to='Questao', related_name="respostas", null=False, blank=False) #onetomany
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4,decimal_places=2)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.DateField()

    def __str__(self):
        return "{} - {}: {}".format(self.questao.id, self.aluno.ra, self.descricao)

    class Meta:
        db_table = 'Resposta'

class ArquivosResposta(models.Model):
    resposta = models.ForeignKey(to='Resposta', related_name="arquivosResposta", null=False, blank=False) #onetomany
    arquivo = models.CharField(max_length=500)

    def __str__(self):
        return "{}: {}".format(self.resposta, self.id)

    class Meta:
        db_table = 'ArquivosResposta'                                                


