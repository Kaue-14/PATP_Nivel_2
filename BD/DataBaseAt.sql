CREATE DATABASE consultorio_psicologia;
USE consultorio_psicologia;

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT, 
    nome_pessoa VARCHAR(100) NOT NULL,  
    data_nascimento DATE NOT NULL,
    sexo ENUM('M', 'F') NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,  
    email VARCHAR(100),  
    senha VARCHAR(255) NOT NULL, 
    telefone VARCHAR(15),
    endereco VARCHAR(255),
    tipo ENUM('admin', 'psicologo', 'paciente') DEFAULT 'paciente',  
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pacientes (
    id_paciente INT PRIMARY KEY,  
    historico_consultas TEXT,  
    possui_alergias ENUM('sim', 'nao') NOT NULL DEFAULT 'nao',  
    descricao_alergias TEXT,  
    possui_plano_saude ENUM('sim', 'nao') NOT NULL DEFAULT 'nao'  
);

ALTER TABLE pacientes 
ADD CONSTRAINT fk_paciente_usuario
FOREIGN KEY (id_paciente) REFERENCES usuarios(id_usuario);

CREATE TABLE psicologos (
    id_psicologo INT PRIMARY KEY,
    FOREIGN KEY (id_psicologo) REFERENCES usuarios(id_usuario),
    especialidade VARCHAR(100),
    registro_profissional VARCHAR(20),
    experiencia TEXT,
    horario_atendimento VARCHAR(255)
);

ALTER TABLE psicologos MODIFY COLUMN id_psicologo INT AUTO_INCREMENT;


CREATE TABLE agendamentos (
    id_agendamento INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT,
    id_psicologo INT,
    data_hora DATETIME NOT NULL,
    status ENUM('agendado', 'cancelado', 'concluído') DEFAULT 'agendado',
    observacoes TEXT,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_psicologo) REFERENCES psicologos(id_psicologo)
);

INSERT INTO usuarios (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES 
('Frantiescoli', '2024-04-05', 'M', '03553845074', 'frantiescoli.froner@gmail.com', 'frantiescoli01', '054996503459', 'Rua Jorge Cafruni, Roselândia', 'admin'),
INSERT INTO usuarios (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('Dr. João Silva', '1980-03-10', 'M', '1234567019', 'joao.silva@gmail.com', 'senha_hash_aqui', '054998765432', 'Rua Psicologia, 123', 'psicologo');

INSERT INTO usuarios (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('Maria Souza', '1992-06-15', 'F', '98765432100', 'maria.souza@gmail.com', 'senha_segura', '054987654321', 'Rua Paciente, 45', 'paciente')

INSERT INTO usuarios (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('Carlos Mendes', '1985-08-20', 'M', '01234567890', 'carlos.mendes@gmail.com', 'carlos123', '054912345678', 'Rua Clinica, 98', 'paciente')

INSERT INTO usuarios (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES ('Ana Clara', '1995-12-10', 'F', '45678912300', 'ana.clara@gmail.com', 'senha_ana', '054954321987', 'Rua Terapia, 789', 'paciente');

INSERT INTO pacientes (id_paciente, historico_consultas, possui_alergias, descricao_alergias, possui_plano_saude)
VALUES 
(3, 'Consulta inicial realizada em 2024', 'nao', '', 'sim'),
(4, 'Histórico limpo', 'nao', '', 'nao'),
(5, 'Consulta de rotina realizada em 2024', 'sim', 'Alergia a penicilina', 'sim');

INSERT INTO psicologos (id_psicologo, especialidade, registro_profissional, experiencia, horario_atendimento)
VALUES 
(3, 'Psicologia Clínica', 'CRP123456', '10 anos de experiência em terapias...', 'Seg-Sex 08:00-18:00'),
(1, 'Psicoterapia', 'CRP654321', '8 anos de experiência em psicoterapia', 'Seg-Sex 09:00-17:00');

INSERT INTO agendamentos (id_paciente, id_psicologo, data_hora, observacoes)
VALUES 
(3, 2, '2024-10-10 15:00:00', 'Consulta de rotina'),
(4, 2, '2024-10-11 09:00:00', 'Primeira consulta'),
(5, 1, '2024-10-12 11:00:00', 'Consulta de acompanhamento'),
(3, 1, '2024-10-13 14:00:00', 'Sessão de terapia cognitiva'),
(4, 2, '2024-10-14 10:00:00', 'Consulta sobre ansiedade');

UPDATE agendamentos
SET data_hora = '2024-10-15 16:00:00'
WHERE id_agendamento = 1;

SELECT * FROM usuarios;
SELECT * FROM pacientes;
SELECT * FROM psicologos;
SELECT * FROM agendamentos;

SELECT a.*, b.*
FROM usuarios a, pacientes b
WHERE a.id_usuario = b.id_paciente;

SELECT a.*, b.*
FROM usuarios a, psicologos b
WHERE a.id_usuario = b.id_psicologo;

SELECT a.*, b.*, c.*, d.*
FROM usuarios a, pacientes b, agendamentos c, usuarios d
WHERE a.id_usuario = b.id_paciente
  AND b.id_paciente = c.id_paciente
  AND c.id_psicologo = d.id_usuario;
