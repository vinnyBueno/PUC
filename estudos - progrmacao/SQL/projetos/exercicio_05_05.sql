drop table if exists  pedidos, clientes;

#A
CREATE TABLE clientes(
	id int not null auto_increment primary key,
    nome varchar(50),
    email varchar(100),
    telefone varchar(15)
);

#B
CREATE TABLE pedidos(
	id int not null  auto_increment primary key,
    cliente_id int,
    data varchar(10),
    total int,
    foreign key (cliente_id) references clientes(id)
    );

#C
INSERT INTO clientes (nome, email, telefone)
VALUES ('João Silva', 'joao@email.com', '11999999999');

#D
INSERT INTO pedidos (cliente_id, data, total)
VALUES 
(1,'2024-01-01', 100),
(1,'2024-01-02', 200);

CREATE TABLE produtos(
	id int not null auto_increment primary key,
    nome varchar(50),
    preco decimal(7,2)
);

CREATE TABLE itens_pedido(
	id int not null auto_increment primary key,
    produto_id int not null,
    foreign key (produto_id) references produtos(id)
);