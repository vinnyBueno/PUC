
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

-- Inserindo os departamentos da universidade
INSERT INTO Departamento (Nome_Departamento) VALUES
('Tecnologia da Informação'),
('Engenharia'),
('Ciências Humanas'),
('Saúde');

-- Inserindo professores vinculados a seus respectivos departamentos
INSERT INTO Professor (Nome_Professor, Sobrenome_Professor, Cod_Departamento) VALUES
('Carlos', 'Silva', 1),
('Ana', 'Souza', 1),
('Roberto', 'Oliveira', 2),
('Fernanda', 'Lima', 3),
('Juliana', 'Mendes', 4);

-- Definindo qual professor gerencia cada departamento
UPDATE Departamento SET Cod_Professor_Gerente = 1 WHERE Cod_Departamento = 1;
UPDATE Departamento SET Cod_Professor_Gerente = 3 WHERE Cod_Departamento = 2;
UPDATE Departamento SET Cod_Professor_Gerente = 4 WHERE Cod_Departamento = 3;
UPDATE Departamento SET Cod_Professor_Gerente = 5 WHERE Cod_Departamento = 4;

-- Inserindo disciplinas oferecidas pelos departamentos
INSERT INTO Disciplina (Nome_Disciplina, Carga_Horaria, Cod_Departamento) VALUES
('Banco de Dados', 80, 1),
('Programação', 100, 1),
('Algoritmos', 80, 1),
('Cálculo', 120, 2),
('Física', 100, 2),
('Psicologia', 60, 3),
('Anatomia', 90, 4);

-- Definindo dependências entre disciplinas (pré-requisitos)
INSERT INTO Disciplina_Dependencia VALUES
(2, 3), -- Programação depende de Algoritmos
(1, 2); -- Banco de Dados depende de Programação

-- Relacionando professores às disciplinas que eles lecionam
INSERT INTO Prof_Disciplina VALUES
(1,1),
(2,2),
(2,3),
(3,4),
(3,5),
(4,6),
(5,7);

-- Inserindo cursos oferecidos pela universidade
INSERT INTO Curso (Nome_Curso, Cod_Departamento) VALUES
('Sistemas de Informação', 1),
('Engenharia Civil', 2),
('Psicologia', 3),
('Enfermagem', 4);

-- Associando disciplinas aos cursos
INSERT INTO Curso_Disciplina VALUES
(1,1),(2,1),(3,1),
(4,2),(5,2),
(6,3),
(7,4);

-- Inserindo alunos matriculados na universidade
INSERT INTO Aluno (Nome_Aluno, Sobrenome_Aluno, CPF, Sexo, Cod_Curso) VALUES
('João', 'Pereira', '11111111111', 'M', 1),
('Maria', 'Costa', '22222222222', 'F', 1),
('Lucas', 'Almeida', '33333333333', 'M', 2),
('Beatriz', 'Santos', '44444444444', 'F', 3),
('Pedro', 'Rocha', '55555555555', 'M', 4);

-- Inserindo telefones dos alunos (atributo multivalorado)
INSERT INTO Aluno_Telefone VALUES
(1,'19999999999'),
(1,'19888888888'),
(2,'19777777777'),
(3,'19666666666');

-- Criando turmas para organização de alunos em períodos
INSERT INTO Turma (Cod_Curso, Cod_Departamento, Periodo) VALUES
(1,1,'2024-1'),
(2,2,'2024-1'),
(3,3,'2024-1');

-- Relacionando alunos às turmas
INSERT INTO Esta_Matriculado VALUES
(1,1),
(2,1),
(3,2),
(4,3);

-- Criando histórico acadêmico para cada aluno
INSERT INTO Historico (RA, Periodo_Realizacao) VALUES
(1,'2023-2'),
(2,'2023-2'),
(3,'2023-2'),
(4,'2023-2');

-- Inserindo notas e frequência dos alunos nas disciplinas
INSERT INTO Disc_Hist VALUES
(1,1,8.5,90),
(1,2,7.0,85),
(2,1,9.0,95),
(3,4,6.0,70),
(4,6,8.0,88);

-- identificar os melhores alunos da universidade 
-- Calcula a média das notas de cada aluno e ordena do maior para o menor
SELECT A.Nome_Aluno, ROUND(AVG(DH.Nota), 1) AS Media
FROM Aluno A
JOIN Historico H ON A.RA = H.RA
JOIN Disc_Hist DH ON H.Cod_Historico = DH.Cod_Historico
GROUP BY A.RA
ORDER BY Media DESC;

-- identificar os professores com maior carga de ensino
-- Conta quantas disciplinas cada professor leciona
SELECT P.Nome_Professor, COUNT(*) AS Total_Disciplinas
FROM Professor P
JOIN Prof_Disciplina PD ON P.Cod_Professor = PD.Cod_Professor
GROUP BY P.Cod_Professor
ORDER BY Total_Disciplinas DESC;

-- descobrir os cursos mais populares
-- Conta quantos alunos existem em cada curso
SELECT C.Nome_Curso, COUNT(A.RA) AS Total_Alunos
FROM Curso C
JOIN Aluno A ON C.Cod_Curso = A.Cod_Curso
GROUP BY C.Cod_Curso
ORDER BY Total_Alunos DESC;

-- identificar alunos que precisam de atenção acadêmica 
-- Filtra alunos com média inferior a 7
SELECT A.Nome_Aluno, ROUND(AVG(DH.Nota), 1) AS Media
FROM Aluno A
JOIN Historico H ON A.RA = H.RA
JOIN Disc_Hist DH ON H.Cod_Historico = DH.Cod_Historico
GROUP BY A.RA
HAVING ROUND(AVG(DH.Nota), 1) < 7; 

-- entender a estrutura de progressão do curso
-- Mostra quais disciplinas possuem dependências
SELECT D.Nome_Disciplina, DP.Cod_Disciplina_Pre
FROM Disciplina D
JOIN Disciplina_Dependencia DP 
ON D.Cod_Disciplina = DP.Cod_Disciplina;

-- identificar alunos com mais de um contato cadastrado
-- Conta quantos telefones cada aluno possui
SELECT RA, COUNT(*) AS Qtd_Telefones
FROM Aluno_Telefone
GROUP BY RA
HAVING COUNT(*) > 1;

-- identificar líderes acadêmicos
-- Mostra professores que gerenciam departamentos
SELECT P.Nome_Professor, D.Nome_Departamento
FROM Professor P
JOIN Departamento D 
ON P.Cod_Professor = D.Cod_Professor_Gerente;

-- avaliar dificuldade ou desempenho geral das matérias
-- Calcula a média das notas em cada disciplina
SELECT D.Nome_Disciplina, ROUND(AVG(DH.Nota), 1) AS Media
FROM Disciplina D
JOIN Disc_Hist DH ON D.Cod_Disciplina = DH.Cod_Disciplina
GROUP BY D.Cod_Disciplina; 

-- visualizar o contexto acadêmico completo do estudante
-- Junta informações completas do aluno
SELECT A.Nome_Aluno, C.Nome_Curso, D.Nome_Departamento
FROM Aluno A
JOIN Curso C ON A.Cod_Curso = C.Cod_Curso
JOIN Departamento D ON C.Cod_Departamento = D.Cod_Departamento;

-- identificar alunos mais frequente
-- Encontra a maior frequência registrada por aluno
SELECT A.Nome_Aluno, MAX(DH.Frequencia) AS Melhor_Frequencia
FROM Aluno A
JOIN Historico H ON A.RA = H.RA
JOIN Disc_Hist DH ON H.Cod_Historico = DH.Cod_Historico
GROUP BY A.RA
ORDER BY Melhor_Frequencia DESC;

-- identificar alunos com desempenho perfeito
-- Seleciona alunos que não possuem nenhuma nota abaixo de 7
SELECT A.Nome_Aluno
FROM Aluno A
WHERE NOT EXISTS (
    SELECT *
    FROM Disc_Hist DH
    JOIN Historico H ON DH.Cod_Historico = H.Cod_Historico
    WHERE H.RA = A.RA AND DH.Nota < 7
);

-- identificar as matérias mais difíceis do curso
-- Ordena disciplinas pela menor média de nota
SELECT D.Nome_Disciplina, ROUND(AVG(DH.Nota), 1) AS Media
FROM Disciplina D
JOIN Disc_Hist DH ON D.Cod_Disciplina = DH.Cod_Disciplina
GROUP BY D.Cod_Disciplina
ORDER BY Media ASC; 