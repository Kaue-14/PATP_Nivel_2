CREATE DATABASE banco_de_dados_agendamento_psicologia;

USE banco_de_dados_agendamento_psicologia;

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,  -- chave primária
    nome varchar(20) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo ENUM('M', 'F') NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,  
    email VARCHAR(100),
    senha VARCHAR(255) NOT NULL,  -- senhas devem ser armazenadas com hashing
    telefone VARCHAR(15),
    endereco VARCHAR(255),
    tipo ENUM('admin', 'psicologo', 'paciente') DEFAULT 'paciente',  -- dferencia entre paciente e psicólogo
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

show tables