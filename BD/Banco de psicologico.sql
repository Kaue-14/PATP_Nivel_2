CREATE DATABASE Banco_de_psicologico;

USE Banco_de_psicologico;

CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,  -- chave primária
    nome varchar(20) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo ENUM('M', 'F') NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,  
    email VARCHAR(100),
    senha VARCHAR(255) NOT NULL,  -- senhas devem ser armazenadas com hashing
    telefone VARCHAR(15),
    endereco VARCHAR(255),
    categoria ENUM('admin', 'Psicólogo(a)', 'Paciente') DEFAULT 'paciente',  -- dferencia entre paciente e psicólogo
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Usuarios (nome, data_nascimento, sexo, cpf, email, senha, telefone, endereco, categoria)
VALUES ('admin', '2000-01-01', 'F', '00000000000', 'admin@gmail.com', 'admin', '00000000000', 'Rua admin, 00', 'admin');

select * from Usuarios;

Update Usuarios set categoria = 'admin' where id_usuario = '2';