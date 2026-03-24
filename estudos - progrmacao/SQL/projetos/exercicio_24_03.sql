CREATE TABLE funcionario(
	cod int not null AUTO_INCREMENT PRIMARY KEY,
    nome varchar(40),
    salario decimal(9,2),
    cargo varchar(30),
    coddepto int,
    comissao decimal(9,2)
);

CREATE TABLE requisicao(
	codreq int(3) not null AUTO_INCREMENT PRIMARY KEY,
    codfunc int(3) not null,
    datareq date
);

INSERT INTO funcionario
values
(111, "JOAO", 1000.00, "Analista de Sistemas", 111, 100.00),
(222,"ANA", 2000.00, "Vendedora", 222, 200.00),
(333."LUIS",3000.00, "Analista de Sistemas", 111, 300.00

drop table funcionario, requisicao;