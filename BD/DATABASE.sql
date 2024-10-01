------------Banco de dados DBA Frantiescoli------------
------------Nao mexer nos comentarios-------------

CREATE DATABASE consultorio_psicologia;

USE consultorio_psicologia;

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,  -- chave primária
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

CREATE INDEX idx_usuarios_cpf on usuarios (cpf);


CREATE TABLE pacientes (
    id_paciente INT PRIMARY KEY,  -- chave primária
    FOREIGN KEY (id_paciente) REFERENCES usuarios(id_usuario)  -- id_paciente é chave estrangeira, primária na tabela usuarios
);


CREATE TABLE psicologos (
    id_psicologo INT PRIMARY KEY,  -- chave primária
    FOREIGN KEY (id_psicologo) REFERENCES usuarios(id_usuario)  -- id_psicologo é chave estrangeira, primária na tabela usuarios
);


CREATE TABLE agendamentos (
    id_agendamento INT PRIMARY KEY AUTO_INCREMENT,  -- chave primaria
    id_paciente INT NOT NULL,  -- chave estrangeira que referencia a tabela pacientes
    id_psicologo INT NOT NULL,  -- chave estrangeira que referencia a tabela psicologos
    data_agendamento DATE NOT NULL,
    hora_agendamento TIME NOT NULL,
    descricao TEXT,
    status ENUM('agendado', 'cancelado', 'concluido') DEFAULT 'agendado',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- Chave estrangeira id_paciente referenciando a chave primária id_paciente na tabela pacientes
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    -- Chave estrangeira id_psicologo referenciando a chave primária id_psicologo na tabela psicologos
    FOREIGN KEY (id_psicologo) REFERENCES psicologos(id_psicologo)
);


CREATE TABLE servicos (
    id_servico INT PRIMARY KEY AUTO_INCREMENT,  -- Chave primária desta tabela
    nome_servico VARCHAR(100) NOT NULL,
    descricao TEXT
    
);

INSERT INTO usuarios (nome, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('Kaue', '2005-12-14', 'M', '01858544900', 'kaue@gmail.com', '01234', '05499231202', 'Rua do Veveco, 54', 'Psicologo');
INSERT INTO usuarios (nome, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('Kaue', '2005-12-14', 'M', '01858544900', 'kaue@gmail.com', '01234', '05499231202', 'Rua do Veveco, 54', 'Psicologo');


INSERT INTO usuarios (nome, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('João Paciente', '1990-02-10', 'M', '09876543210', 'joao@example.com', 'senhaPacienteHasheada', '11988888888', 'Avenida Teste, 200', 'paciente');


INSERT INTO psicologos (id_psicologo) SELECT id_usuario FROM usuarios WHERE cpf = '01858544900';
INSERT INTO pacientes (id_paciente) SELECT id_usuario FROM usuarios WHERE cpf = '09876543210';



update  usuarios
set data_nascimento = '2005-12-12'
where cpf = '01858544900'


insert into agendamentos (id_agendamento, id_paciente, id_psicologo, data_agendamento, descricao, status)
values                   (1,001, 10, '2024-02-10' , 'Consulta de emergencia', 'agendado')

insert into paciente (id_paciente) select

select * from pacientes;

select * from usuarios;

select * from servicos;

select * from agendamentos;

select * from psicologos;

insert into pacientes (id_paciente) values (010)


