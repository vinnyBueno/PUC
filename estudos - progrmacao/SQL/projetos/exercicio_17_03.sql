DROP TABLE alunos;
DROP TABLE produtos;
DROP TABLE funcionarios;
DROP TABLE livros;
DROP TABLE clientes;
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


INSERT INTO produtos 
VALUES 
(DEFAULT, 'celular', 100.50, 1000),
(DEFAULT, 'televisão', 400.00, 50),
(DEFAULT, 'garrafa', 25.99, 0),
(DEFAULT, 'tenis', 650.90, 35);

UPDATE produtos
SET preco = preco * 1.10
WHERE id_produto = 1;

DELETE FROM produtos WHERE estoque = 0 AND id_produto = 3;


/*----Exercício 3- Cadastro de funcionários------*/
CREATE TABLE funcionarios(
	id_funcionario int not null AUTO_INCREMENT PRIMARY KEY,
    nome varchar(100),
    cargo varchar(50),
    salario decimal(8,2)
);

INSERT INTO funcionarios
values
(DEFAULT, 'Pedro', 'analista', 1500.00),
(DEFAULT, 'Vinicius', 'engenheiro de dados', 850.00),
(DEFAULT, 'Bruna', 'Project owner','16300.00'),
(DEFAULT, 'Raquel', 'tech lead', '40000.00'),
(DEFAULT, 'Rafaela', 'CEO', '100000.00');

UPDATE funcionarios
set salario = salario + 500.00
WHERE cargo = 'analista' AND id_funcionario = 1;

DELETE FROM funcionarios WHERE salario < 2000.00 AND id_funcionario = 1;
DELETE FROM funcionarios WHERE salario < 2000.00 AND id_funcionario = 2;

/*----Exercício 4- Cadastro de funcionários------*/
CREATE TABLE livros(
	id_livro int not null AUTO_INCREMENT PRIMARY KEY,
    titulo varchar(150) not null,
    autor varchar(100) not null,
    ano_publicado int not null
);

INSERT INTO livros 
VALUES
(DEFAULT,'Dom Casmurro','Machado de Assis',1899),
(DEFAULT,'O Pequeno Principe','Antonie de Saint-Exupéry',1943),
(DEFAULT,'1984','George Orwell',1949),
(DEFAULT,'Harry Potter e a Pedra Filosofal','J.K. Rowling',1997);

UPDATE livros
SET ano_publicado = 2026
WHERE id_livro = 2;

DELETE FROM livros WHERE ano_publicado < 2000 and id_livro = 1;
DELETE FROM livros WHERE ano_publicado < 2000 and id_livro = 3;
DELETE FROM livros WHERE ano_publicado < 2000 and id_livro = 4;

/*----Exercício 4- Cadastro de funcionários------*/
CREATE TABLE clientes(
	id_cliente int not null AUTO_INCREMENT PRIMARY KEY,
    nome varchar(100),
    email varchar(100),
    telefone varchar(20)
);

INSERT INTO clientes
VALUES
(DEFAULT,'Carlos Silva', 'carlos.silva@email.com', '(11)91234-5678') ,
(DEFAULT,'Ana Souza', 'ana.souza@email.com','(21)99876-5678'),
(DEFAULT,'João Pereira', 'joao.pereira@email.com','(31)98765-4321'),
(DEFAULT,'Mariana Costa','mariana.costa@gmail.com','(41)97654-3210'),
(DEFAULT,'Lucas Oliveira','lucas.oliveira@email.com', '(51)96543-2109');

UPDATE clientes
SET telefone = '(19)99213-6624'
WHERE id_cliente = 3;

DELETE FROM clientes WHERE email LIKE '%@gmail.com';
