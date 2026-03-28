SET SQL_SAFE_UPDATES = 0;
drop table if exists funcionario, requisicao;


#1-Crie a tabela FUNCIONARIO e insira os seguintes registros, de acordo com o exemplo abaixo#
CREATE TABLE funcionario(
	cod int not null AUTO_INCREMENT PRIMARY KEY,
    nome varchar(40),
    salario decimal(9,2),
    cargo varchar(30),
    coddepto int,
    comissao decimal(9,2)
);


INSERT INTO funcionario
values
(111, "JOAO", 1000.00, "Analista de Sistemas", 111, 100.00),
(222,"ANA", 2000.00, "Vendedora", 222, 200.00),
(333,"LUIS",3000.00, "Analista de Sistemas", 111, 300.00),
(144,"MARIA",1500.00, "Analista de Sistemas",111, 100.00),
(515, "ANGELA", 900.00,"Vendedora", 222, 200.00),
(166, "LUIS RICARDO", 5000.00, "Analista de Sistemas", 111, 300.00);

#2 Crie a tabela REQUISICAO e insira os seguintes registros, de acordo com o exemplo abaixo:#
CREATE TABLE requisicao(
	codreq int(3) not null AUTO_INCREMENT PRIMARY KEY,
    codfunc int(3) not null,
    datareq date
);

INSERT INTO requisicao
values
(1, 111,'2004-05-01'),
(2,222,'2004-05-15'),
(3,111,'2004-05-10');

#3 Selecione todas as colunas da tabela FUNCIONARIO#
select * from funcionario;

#4 Quais os códigos e nomes dos funcionários que possuem salário maior que $1000,00?
SELECT cod, nome from funcionario where salario > 1000.00;

#5 Selecione os códigos, nomes e salários dos funcionários que possuem salário entre $1000,00 e $2000,00 (inclusive).
SELECT cod, nome, salario from funcionario where salario >= 1000.00 and salario <= 2000.00;