DROP TABLE alunos;
/*----Exercício 1 - Cadastro de Alunos------*/
CREATE TABLE alunos(
	id_aluno int not null AUTO_INCREMENT PRIMARY KEY,
    nome varchar(100) not null,
    idade int not null,
    cidade varchar(50)
);

INSERT INTO alunos (id_aluno, nome, idade, cidade )
values 
(1,'Pedro da Silva', 18, 'tatui'),
(DEFAULT,'Joaquim da Silva', 10, 'Rio de Janeiro'),
(DEFAULT,'Maria Santos', 20, 'tatui');


UPDATE alunos
SET cidade = "Rio de janeiro"
where id_aluno = 3;

DELETE FROM alunos WHERE idade < 18 and id_aluno = 2;


/*----Exercício 2- Cadastro de produtos------*/
CREATE TABLE produtos(
	id_produto int not null AUTO_INCREMENT PRIMARY KEY,
    nome_produto varchar(100) not null,
    preco decimal(5,2),
    estoque int
);