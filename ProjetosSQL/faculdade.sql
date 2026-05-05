create database tbl_faculdade;
use tbl_faculdade;

create table tbl_aluno(
	id_aluno int auto_increment primary key,
    nome varchar(100) not null,
	cpf varchar(14) unique not null,
    email varchar(100) unique not null,
    data_nasc date not null,
    endereco text
    );
    
    create table tbl_professor(
    id_professor int auto_increment primary key,
    nome varchar(100) not null,
    cpf varchar(14) unique not null,
    especializacao varchar(100) not null
    );
    
    create table tbl_curso(
    id_curso int auto_increment primary key,
    nome varchar(100) not null,
    duracao int not null
    );
    
    create table tbl_disciplina(
    id_disciplina int auto_increment primary key,
    nome varchar(100) not null,
    carga_horaria int not null,
    id_curso int not null,
    
    foreign key (id_curso)
    references tbl_curso(id_curso)
    );
    
    create table tbl_turma(
    id_turma int auto_increment primary key,
    codigo_turma varchar(20) unique not null,
    semestre varchar(10) not null,
    id_disciplina int not null,
    id_professor int not null,
    
    foreign key (id_disciplina)
    references tbl_disciplina(id_disciplina),
    
    foreign key (id_professor)
    references tbl_professor(id_professor)
    );
    
    create table tbl_matricula(
    id_matricula int auto_increment primary key,
    nota_final decimal(4.2),
    frequencia decimal(5,2),
    id_aluno int not null,
    id_turma int not null,
    
    foreign key (id_aluno)
    references tbl_aluno (id_aluno),
    
    foreign key (id_turma)
    references tbl_turma (id_turma)
    );
    
    
 