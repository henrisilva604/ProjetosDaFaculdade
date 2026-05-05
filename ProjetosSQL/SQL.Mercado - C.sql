create database supermercado_db;
use supermercado_db;

create table tbl_categoria(
  id_categoria int auto_increment primary key,
  nome varchar(50) not null,
  descricao text
  );
  
  create table tbl_fornecedor( 
  id_fornecedor int auto_increment primary key,
  nome varchar(100) not null,
  cnpj varchar(18) unique not null,
  telefone varchar(15),
  email varchar(100),
  endereco text
  );
  
  create table tbl_cliente(
  id_cliente int auto_increment primary key,
  nome varchar(100) not null,
  cpf varchar(14) unique not null,
  telefone varchar(15),
  email varchar(100),
  endereco text
  );
  
  create table tbl_funcionario(
  id_funcionario int auto_increment primary key,
  nome varchar(100) not null,
  cpf varchar(14) unique not null,
  cargo varchar(50) not null,
  telefone varchar(15),
  data_admissao date not null,
  salario decimal(10,2) not null
  );
  
  create table tbl_produto(
  id_produto int auto_increment primary key,
  nome varchar(100) not null,
  descricao text,
  preco_unitario  decimal(10,2) not null,
  quantidade_estoque int not null default 0,
  id_categoria int not null,
  
 constraint FK_categoria_produto
 FOREIGN KEY (id_categoria)
 REFERENCES tbl_categoria(id_categoria)
);

create table tbl_venda(
  id_venda int auto_increment primary key,
  id_cliente int,
  id_funcionario int not null,
  data_venda datetime not null default current_timestamp,
  valor_total decimal(10,2) not null,
  forma_pagamento varchar(20) not null,
  status varchar(20) not null default 'concluida',
  
   FOREIGN KEY (id_cliente) REFERENCES tbl_cliente(id_cliente),
   FOREIGN KEY (id_funcionario) REFERENCES tbl_funcionario(id_funcionario)
);

CREATE TABLE tbl_item_venda (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_venda) REFERENCES tbl_venda(id_venda),
    FOREIGN KEY (id_produto) REFERENCES tbl_produto(id_produto)
) ;

CREATE TABLE tbl_compra (
    id_compra INT AUTO_INCREMENT PRIMARY KEY,
    id_fornecedor INT NOT NULL,
    data_compra DATE NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pendente',
    FOREIGN KEY (id_fornecedor) REFERENCES tbl_fornecedor(id_fornecedor)
);

CREATE TABLE tbl_item_compra (
    id_item_compra INT AUTO_INCREMENT PRIMARY KEY,
    id_compra INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_compra) REFERENCES tbl_compra(id_compra),
    FOREIGN KEY (id_produto) REFERENCES tbl_produto(id_produto)
);
  
CREATE INDEX idx_produto_nome ON tbl_produto(nome);
CREATE INDEX idx_cliente_cpf ON tbl_cliente(cpf);
CREATE INDEX idx_funcionario_cpf ON tbl_funcionario(cpf);
CREATE INDEX idx_venda_data ON tbl_venda(data_venda);
  

INSERT INTO tbl_categoria (nome, descricao) VALUES 
('Bebidas', 'Refrigerantes, sucos, águas'),
('Limpeza', 'Produtos de limpeza doméstica');

INSERT INTO tbl_fornecedor (nome, cnpj, telefone) VALUES
('Coca-Cola Brasil', '12.345.678/0001-99', '(11) 1234-5678');

INSERT INTO tbl_produto (nome, preco_unitario, quantidade_estoque, id_categoria) VALUES
('Coca-Cola 2L', 8.99, 100, 1),
('Sabão em Pó OMO', 12.50, 50, 2);
