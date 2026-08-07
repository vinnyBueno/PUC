DROP TABLE IF EXISTS produto, cliente, pedido;

CREATE TABLE produto (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
preco DECIMAL(10,2),
categoria VARCHAR(50)
);
CREATE TABLE cliente (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
cidade VARCHAR(100),
idade INT
);
CREATE TABLE pedido (
id INT AUTO_INCREMENT PRIMARY KEY,
cliente_id INT,
valor_total DECIMAL(10,2),
data_pedido DATE
);


INSERT INTO produto (nome, preco, categoria) VALUES
('Notebook', 3500.00, 'Eletrônicos'),
('Smartphone', 2000.00, 'Eletrônicos'),
('Cadeira', 450.00, 'Móveis'),
('Mesa', 800.00, 'Móveis'),
('Carregador',800.00,'Acessórios'),
('Fone de Ouvido', 150.00, 'Acessórios');


INSERT INTO cliente (nome, cidade, idade) VALUES
('João Silva', 'São Paulo', 30),
('Maria Souza', 'Rio de Janeiro', 25),
('Carlos Lima', 'Belo Horizonte', 40),
('Ana Costa', 'Curitiba', 28),
('Rafa','Campinas', 19),
('Raquel','Campinas', 18),
('Bruna','Campinas',19),
('Pedro Rocha', 'Salvador', 35);


INSERT INTO pedido (cliente_id, valor_total, data_pedido) VALUES
(1, 3500.00, '2024-01-10'),
(2, 2000.00, '2024-01-12'),
(3, 1250.00, '2024-01-15'),
(1, 150.00, '2024-01-20'),
(4, 800.00, '2024-02-01'),
(5, 450.00, '2024-02-05');

SELECT nome from cliente where idade > (select avg(idade) from cliente);

SELECT nome, preco from produto where preco >= (select avg(preco) from produto);

SELECT nome from cliente where cidade in (select cidade from cliente group by cidade having count(*) = 1);

SELECT nome from produto where preco = (select preco from produto group by preco having count(preco) > 1);

SELECT * from pedido where valor_total > (SELECT max(valor_total) from pedido where data_pedido >= "2023-01-01" and data_pedido <= "2023-12-31"); 

SELECT nome from cliente where id not in (SELECT cliente_id from pedido);