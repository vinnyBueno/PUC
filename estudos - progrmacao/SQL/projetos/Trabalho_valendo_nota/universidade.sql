
--  CRIAÇÃO DO BANCO DE DADOS — SISTEMA UNIVERSITÁRIO



-- DEPARTAMENTO
CREATE TABLE Departamento (
    Cod_Departamento  INT          NOT NULL AUTO_INCREMENT,
    Nome_Departamento VARCHAR(100) NOT NULL,
    PRIMARY KEY (Cod_Departamento)
);


-- PROFESSOR
CREATE TABLE Professor (
    Cod_Professor        INT         NOT NULL AUTO_INCREMENT,
    Nome_Professor       VARCHAR(80) NOT NULL,
    Sobrenome_Professor  VARCHAR(80) NOT NULL,
    Status               VARCHAR(30) NOT NULL DEFAULT 'Ativo',
    Cod_Departamento     INT         NOT NULL,
    PRIMARY KEY (Cod_Professor),
    CONSTRAINT fk_prof_depto
        FOREIGN KEY (Cod_Departamento) REFERENCES Departamento (Cod_Departamento)
);

-- Gerencia: um Departamento é gerenciado por exatamente 1 Professor
ALTER TABLE Departamento
    ADD COLUMN Cod_Professor_Gerente INT NULL,
    ADD CONSTRAINT fk_depto_gerente
        FOREIGN KEY (Cod_Professor_Gerente) REFERENCES Professor (Cod_Professor);


-- DISCIPLINA
CREATE TABLE Disciplina (
    Cod_Disciplina   INT          NOT NULL AUTO_INCREMENT,
    Nome_Disciplina  VARCHAR(100) NOT NULL,
    Carga_Horaria    INT          NOT NULL,
    Descricao        TEXT,
    Num_Alunos       INT          DEFAULT 0,
    Cod_Departamento INT          NOT NULL,
    PRIMARY KEY (Cod_Disciplina),
    CONSTRAINT fk_disc_depto
        FOREIGN KEY (Cod_Departamento) REFERENCES Departamento (Cod_Departamento)
);

-- Depende: auto-relacionamento de pré-requisito (0,n):(0,n)
CREATE TABLE Disciplina_Dependencia (
    Cod_Disciplina     INT NOT NULL,
    Cod_Disciplina_Pre INT NOT NULL,
    PRIMARY KEY (Cod_Disciplina, Cod_Disciplina_Pre),
    CONSTRAINT fk_dep_disc
        FOREIGN KEY (Cod_Disciplina)     REFERENCES Disciplina (Cod_Disciplina),
    CONSTRAINT fk_dep_pre
        FOREIGN KEY (Cod_Disciplina_Pre) REFERENCES Disciplina (Cod_Disciplina)
);


-- PROF_DISCIPLINA
CREATE TABLE Prof_Disciplina (
    Cod_Professor  INT NOT NULL,
    Cod_Disciplina INT NOT NULL,
    PRIMARY KEY (Cod_Professor, Cod_Disciplina),
    CONSTRAINT fk_pd_prof
        FOREIGN KEY (Cod_Professor)  REFERENCES Professor  (Cod_Professor),
    CONSTRAINT fk_pd_disc
        FOREIGN KEY (Cod_Disciplina) REFERENCES Disciplina (Cod_Disciplina)
);


-- CURSO
CREATE TABLE Curso (
    Cod_Curso        INT          NOT NULL AUTO_INCREMENT,
    Nome_Curso       VARCHAR(100) NOT NULL,
    Cod_Departamento INT          NOT NULL,
    PRIMARY KEY (Cod_Curso),
    CONSTRAINT fk_curso_depto
        FOREIGN KEY (Cod_Departamento) REFERENCES Departamento (Cod_Departamento)
);


-- CURSO_DISCIPLINA  
CREATE TABLE Curso_Disciplina (
    Cod_Disciplina INT NOT NULL,
    Cod_Curso      INT NOT NULL,
    PRIMARY KEY (Cod_Disciplina, Cod_Curso),
    CONSTRAINT fk_cd_disc
        FOREIGN KEY (Cod_Disciplina) REFERENCES Disciplina (Cod_Disciplina),
    CONSTRAINT fk_cd_curso
        FOREIGN KEY (Cod_Curso)      REFERENCES Curso      (Cod_Curso)
);


-- ALUNO
CREATE TABLE Aluno (
    RA              INT          NOT NULL AUTO_INCREMENT,
    Nome_Aluno      VARCHAR(80)  NOT NULL,
    Sobrenome_Aluno VARCHAR(80)  NOT NULL,
    CPF             CHAR(11)     NOT NULL UNIQUE,
    Status          VARCHAR(30)  NOT NULL DEFAULT 'Ativo',
    Sexo            CHAR(1),
    Filiacao        VARCHAR(150),
    Rua             VARCHAR(150),
    Num             VARCHAR(10),
    CEP             CHAR(8),
    Endereco        VARCHAR(200),  -- endereço completo (atributo composto)
    Contato         VARCHAR(100),  -- atributo simples/derivado
    Cod_Curso       INT          NOT NULL,
    PRIMARY KEY (RA),
    CONSTRAINT fk_aluno_curso
        FOREIGN KEY (Cod_Curso) REFERENCES Curso (Cod_Curso)
);

-- Telefone: atributo multivalorado
CREATE TABLE Aluno_Telefone (
    RA       INT         NOT NULL,
    Telefone VARCHAR(20) NOT NULL,
    PRIMARY KEY (RA, Telefone),
    CONSTRAINT fk_tel_aluno
        FOREIGN KEY (RA) REFERENCES Aluno (RA)
);


-- TURMA
CREATE TABLE Turma (
    Cod_Turma        INT         NOT NULL AUTO_INCREMENT,
    Cod_Curso        INT         NOT NULL,
    Cod_Departamento INT         NOT NULL,
    Periodo          VARCHAR(10) NOT NULL,
    Data_Inicio      DATE,
    Data_Fim         DATE,
    Num_Alunos       INT         DEFAULT 0,
    PRIMARY KEY (Cod_Turma),
    CONSTRAINT fk_turma_curso
        FOREIGN KEY (Cod_Curso)        REFERENCES Curso        (Cod_Curso),
    CONSTRAINT fk_turma_depto
        FOREIGN KEY (Cod_Departamento) REFERENCES Departamento (Cod_Departamento)
);


-- ESTÁ MATRICULADO  
CREATE TABLE Esta_Matriculado (
    RA        INT NOT NULL,
    Cod_Turma INT NOT NULL,
    PRIMARY KEY (RA, Cod_Turma),
    CONSTRAINT fk_mat_aluno
        FOREIGN KEY (RA)        REFERENCES Aluno  (RA),
    CONSTRAINT fk_mat_turma
        FOREIGN KEY (Cod_Turma) REFERENCES Turma  (Cod_Turma)
);


-- HISTÓRICO
CREATE TABLE Historico (
    Cod_Historico      INT         NOT NULL AUTO_INCREMENT,
    RA                 INT         NOT NULL UNIQUE,   -- (1,1) cada aluno tem 1 histórico
    Periodo_Realizacao VARCHAR(10),
    PRIMARY KEY (Cod_Historico),
    CONSTRAINT fk_hist_aluno
        FOREIGN KEY (RA) REFERENCES Aluno (RA)
);


-- DISC_HIST
CREATE TABLE Disc_Hist (
    Cod_Historico  INT            NOT NULL,
    Cod_Disciplina INT            NOT NULL,
    Nota           DECIMAL(5,2),
    Frequencia     DECIMAL(5,2),
    PRIMARY KEY (Cod_Historico, Cod_Disciplina),
    CONSTRAINT fk_dh_hist
        FOREIGN KEY (Cod_Historico)  REFERENCES Historico  (Cod_Historico),
    CONSTRAINT fk_dh_disc
        FOREIGN KEY (Cod_Disciplina) REFERENCES Disciplina (Cod_Disciplina)
);


-- ALUNO_DISC
CREATE TABLE Aluno_Disc (
    Cod_Aluno      INT NOT NULL,
    Cod_Disciplina INT NOT NULL,
    PRIMARY KEY (Cod_Aluno, Cod_Disciplina),
    CONSTRAINT fk_ad_aluno
        FOREIGN KEY (Cod_Aluno)      REFERENCES Aluno      (RA),
    CONSTRAINT fk_ad_disc
        FOREIGN KEY (Cod_Disciplina) REFERENCES Disciplina (Cod_Disciplina)
);

