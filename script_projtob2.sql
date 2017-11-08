/* Cria��o da database projetob2*/
create database projetob2

/* Usando a database projetob2*/
use projetob2 
go

/* Teste

select * from GradeCurricular

use master
go
drop database projetob2
go

alter table Aluno
DROP CONSTRAINT pk_Aluno

drop table Aluno

*/

/* Cria��o da tabela Curso*/
create table Curso(
	sigla varchar(5) not null,
	nome varchar(50) not null,
	constraint pk_Curso primary key (sigla),
	constraint uc_nome unique (nome)
)

/* Cria��o da tabela Grade Curricular*/
create table GradeCurricular(
	sigla_curso varchar(5) not null,
	ano smallint not null,
	semestre char(1) not null,
	constraint pk_GradeCurricular primary key (sigla_curso, ano, semestre),
	constraint fk_GradeCurricular_Curso foreign key (sigla_curso)
	references Curso(sigla)
)

/* Cria��o da tabela Per�odo*/
create table Periodo(
	sigla_curso varchar(5) not null,
	ano_grade smallint not null,
	semestre_grade char(1) not null,
	numero tinyint not null,
	constraint pk_Periodo primary key (sigla_curso, ano_grade, semestre_grade, numero),
	constraint fk_Periodo_GradeCurricular foreign key (sigla_curso, ano_grade, semestre_grade)
	references GradeCurricular(sigla_curso, ano, semestre)
)

/* Cria��o da tabela Disciplina*/
create table Disciplina(
	nome varchar(240) not null,
	carga_horaria tinyint not null,
	teoria decimal(3) not null,
	pratica decimal(3) not null,
	ementa text,
	competencias text,
	habilidades text,
	conteudo text,
	bibliografia_basica text,
	bibliografia_complementar text,
	constraint pk_disciplina primary key (nome)
)

/* Cria��o da tabela PeriodoDisciplina*/
create table PeriodoDisciplina(
	sigla_curso varchar(5) not null,
	ano_grade smallint not null,
	semestre_grade char(1) not null,
	numero_periodo tinyint not null,
	nome_disciplina varchar(240) not null,
	constraint pk_PeriodoDisciplina_Periodo primary key (sigla_curso, ano_grade, semestre_grade, numero_periodo, nome_disciplina),
	constraint fk_PeriodoDisciplina_Periodo foreign key (sigla_curso, ano_grade, semestre_grade, numero_periodo)
	references Periodo(sigla_curso, ano_grade, semestre_grade, numero),
	constraint fk_PeriodoDisciplina_Disciplina foreign key (nome_disciplina)
	references Disciplina(nome)
)

/* Cria��o da tabela Aluno*/
create table Aluno(
	ra int not null,
	nome varchar(120) not null,
	email varchar(80),
	celular char(11),
	sigla_curso varchar(5) not null,
	constraint pk_Aluno primary key(ra),
	constraint fk_Aluno_Curso foreign key (sigla_curso)
	references Curso(sigla)
)

/* Cria��o da tabela DisciplinaOfertada*/
create table DisciplinaOfertada(
	nome_disciplina varchar(240) not null,
	ano smallint not null,
	semestre char(1) not null,
	constraint pk_DisciplinaOfertada primary key (nome_disciplina, ano, semestre),
	constraint fk_DisciplinaOfertada_Disciplina foreign key (nome_disciplina)
	references Disciplina(nome)
)

/* Cria��o da tabela Professor*/
create table Professor(
	ra int not null,
	apelido varchar(30),
	nome varchar(120) not null,
	email varchar(80),
	celular char(11),
	constraint pk_Professor primary key (ra),
	constraint uc_apelido unique (apelido)
)

/* Cria��o da tabela Turma*/
create table Turma(
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id char(1) not null,
	turno varchar(5) not null,
	ra_professor int not null,
	constraint pk_Turma primary key (nome_disciplina, ano_ofertado, semestre_ofertado, id),
	constraint fk_Turma_DisciplinaOfertada foreign key (nome_disciplina, ano_ofertado, semestre_ofertado)
	references DisciplinaOfertada(nome_disciplina, ano, semestre),
	constraint fk_Turma_Professor foreign key (ra_professor)
	references Professor(ra)
)

/* Cria��o da tabela Matr�cula*/
create table Matricula(
	ra_aluno int not null,
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id_turma char(1) not null,
	constraint pk_Matricula primary key (ra_aluno, nome_disciplina, ano_ofertado, semestre_ofertado, id_turma),
	constraint fk_Matricula_Aluno foreign key (ra_aluno)
	references Aluno(ra),
	constraint fk_Matricula_Turma foreign key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma)
	references Turma(nome_disciplina, ano_ofertado, semestre_ofertado, id)
)

/* Cria��o da tabela CursoTurma*/
create table CursoTurma(
	sigla_curso varchar(5) not null,
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id_turma char(1) not null,
	constraint pk_CursoTurma primary key (sigla_curso, nome_disciplina, ano_ofertado, semestre_ofertado, id_turma),
	constraint fk_CursoTurma_Curso foreign key (sigla_curso)
	references Curso(sigla),
	constraint fk_CursoTurma_Turma foreign key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma)
	references Turma(nome_disciplina, ano_ofertado, semestre_ofertado, id)
)

/* Cria��o da tabela Questao*/
create table Questao(
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id_turma char(1) not null,
	numero int,
	data_limite_entrega date,
	descricao text,
	data date,
	constraint pk_Questao primary key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero),
	constraint fk_Questao_Turma foreign key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma)
	references Turma(nome_disciplina, ano_ofertado, semestre_ofertado, id)
)

/* Cria��o da tabela Resposta*/
create table Resposta(
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id_turma char(1) not null,
	numero_questao int,
	ra_aluno int not null,
	data_avaliacao date,
	nota decimal(4,2),
	avaliacao text,
	descricao text,
	data_de_envio date,
	constraint pk_Resposta primary key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao, ra_aluno),
	constraint fk_Resposta_ArquivosResposta foreign key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao)
	references Questao(nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero),
	constraint fk_Resposta_Aluno foreign key (ra_aluno)
	references Aluno(ra)
)

/* Cria��o da tabela ArquivosResposta*/
create table ArquivosResposta(
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id_turma char(1) not null,
	numero_questao int,
	ra_aluno int not null,
	arquivo varchar(500),
	constraint pk_ArquivosResposta primary key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao, ra_aluno, arquivo),
	constraint fk_ArquivosResposta_Resposta foreign key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao, ra_aluno)
	references Resposta(nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao, ra_aluno)
)

/* Cria��o da tabela ArquivosQuestao*/
create table ArquivosQuestao(
	nome_disciplina varchar(240) not null,
	ano_ofertado smallint not null,
	semestre_ofertado char(1) not null,
	id_turma char(1) not null,
	numero_questao int not null, 
	arquivo varchar(500),
	constraint pk_ArquivosQuestao primary key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao, arquivo),
	constraint fk_ArquivosQuestao_Questao foreign key (nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero_questao)
	references Questao(nome_disciplina, ano_ofertado, semestre_ofertado, id_turma, numero)
)



