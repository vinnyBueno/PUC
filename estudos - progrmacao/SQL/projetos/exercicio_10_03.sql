CREATE TABLE autores(
	id_autor int not null auto_increment PRIMARY KEY,
    nome varchar(100),
    pais varchar(100),
    ano_nascimento int);
    
    CREATE TABLE livros(
		id_livro int not null auto_increment PRIMARY KEY,
        titulo varchar(150),
        genero varchar(50),
        ano_publicado int,
        id_autor int,
        FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
    );
    
    CREATE TABLE leitores(
		id_leitor int not null auto_increment PRIMARY KEY,
        nome varchar(100),
        email varchar(100),
        telefone varchar(20)
    );
    
    CREATE TABLE emprestimos(
		id_emprestimos int not null auto_increment PRIMARY KEY,
        id_leitor int not null,
        id_livro int not null,
        data_emprestimo date not null,
        data_devolucao date,
        FOREIGN KEY (id_leitor) REFERENCES leitores(id_leitor),
        FOREIGN KEY (id_livros) REFERENCES livros(id_livro)        
    );
    
    ALTER TABLE livros
    ADD COLUMN quantidade_estoque int;
    
    ALTER TABLE leitores
    ADD COLUMN data_cadastro date;
    
    ALTER TABLE leitores
    MODIFY COLUMN telefone varchar(30);
    
    ALTER TABLE autores
    DROP COLUMN pais;
    
    ALTER TABLE livros
    ADD COLUMN editora varchar(100);
    
    DROP TABLE emprestimos;
    
    DROP TABLE livros;
    
    DROP TABLE autores;