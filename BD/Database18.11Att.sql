CREATE DATABASE consultoriov1;

USE consultoriov1;



CREATE TABLE usuarios1 (
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


CREATE TABLE pacientes1 (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    historico_consultas TEXT,
    possui_alergias ENUM('sim', 'nao') DEFAULT 'nao',
    descricao_alergias TEXT,
    possui_plano_saude ENUM('sim', 'nao') DEFAULT 'nao',
    CONSTRAINT fk_pacientes_usuarios FOREIGN KEY (id_usuario) REFERENCES usuarios1(id_usuario)
);


CREATE TABLE psicologos1 (
    id_psicologo INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    especialidade VARCHAR(100),
    registro_profissional VARCHAR(20),
    experiencia TEXT,
    horario_atendimento VARCHAR(255),
    CONSTRAINT fk_psicologos_usuarios FOREIGN KEY (id_usuario) REFERENCES usuarios1(id_usuario)
);

CREATE TABLE agendamentos1 (
    id_agendamento INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_psicologo INT NOT NULL,
    data_hora DATETIME NOT NULL,
    status ENUM('agendado', 'cancelado', 'concluído') DEFAULT 'agendado',
    observacoes TEXT,
    CONSTRAINT fk_agendamento_paciente FOREIGN KEY (id_paciente) REFERENCES pacientes1(id_paciente),
    CONSTRAINT fk_agendamento_psicologo FOREIGN KEY (id_psicologo) REFERENCES psicologos1(id_psicologo)
);



INSERT INTO usuarios1 (nome_pessoa, data_nascimento, sexo, cpf, email, senha, telefone, endereco, tipo)
VALUES 
('Maria Souza', '1992-06-15', 'F', '98765432100', 'maria.souza@gmail.com', 'senha_segura', '054987654321', 'Rua Paciente, 45', 'paciente'),
('Carlos Mendes', '1985-08-20', 'M', '01234567890', 'carlos.mendes@gmail.com', 'carlos123', '054912345678', 'Rua Clínica, 98', 'paciente'),
('Dr. João Silva', '1980-03-10', 'M', '1234567019', 'joao.silva@gmail.com', 'senha_hash', '054998765432', 'Rua Psicologia, 123', 'psicologo');


INSERT INTO pacientes1 (id_usuario, historico_consultas, possui_alergias, descricao_alergias, possui_plano_saude)
VALUES 
(1, 'Consulta inicial em 2024', 'nao', '', 'sim'),
(2, 'Histórico limpo', 'nao', '', 'nao');


INSERT INTO psicologos1 (id_usuario, especialidade, registro_profissional, experiencia, horario_atendimento)
VALUES 
(3, 'Psicologia Clínica', 'CRP123456', '10 anos de experiência', 'Seg-Sex 08:00-18:00');


INSERT INTO agendamentos1 (id_paciente, id_psicologo, status, observacoes, data, hora)
VALUES 
(1, 1, 'agendado', 'Primeira consulta', '2024-12-04', '08:00');
INSERT INTO agendamentos1 (id_paciente, id_psicologo, status, observacoes, data, hora)
VALUES 
(2, 2, 'agendado', 'Revisao', '2024-09-25', '10:00');


SELECT 
    c.nome_pessoa AS nome_paciente,
    e.nome_pessoa AS nome_psicologo,
    a.data_hora,
    a.status,
    a.observacoes,
    b.historico_consultas,
    d.especialidade
FROM 
    agendamentos1 a, 
    pacientes1 b, 
    usuarios1 c, 
    psicologos1 d, 
WHERE 
    a.id_paciente = b.id_paciente
    AND b.id_usuario = c.id_usuario
    AND a.id_psicologo = d.id_psicologo;

select * from agendamentos1;


ALTER TABLE agendamentos1
ADD COLUMN data DATE NOT NULL,
ADD COLUMN hora TIME NOT NULL;

UPDATE agendamentos1
SET 
    data = DATE(data_hora),  -- Extrai apenas a parte da data
    hora = TIME(data_hora);  -- Extrai apenas a parte da hora

ALTER TABLE agendamentos1
DROP COLUMN data_hora;




delete from agendamentos1 where id_agendamento in (1,2);


select * from agendamentos1;



CREATE OR REPLACE VIEW v_pacientes AS
SELECT 
    id_usuario,
    nome_pessoa,
    TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) AS idade,
    sexo,
    cpf,
    email,
    telefone,
    endereco,
    tipo,
    criado_em
FROM usuarios1
WHERE tipo = 'paciente';


CREATE OR REPLACE VIEW v_psicologo AS
SELECT 
    usuarios1.id_usuario,
    usuarios1.nome_pessoa,
    TIMESTAMPDIFF(YEAR, usuarios1.data_nascimento, CURDATE()) AS idade,
    usuarios1.sexo,
    usuarios1.email,
    usuarios1.telefone,
    usuarios1.cpf,
    usuarios1.endereco,
    psicologos1.id_psicologo,
    psicologos1.especialidade,
    psicologos1.registro_profissional,
    psicologos1.experiencia,
    psicologos1.horario_atendimento
FROM usuarios1, psicologos1
WHERE usuarios1.id_usuario = psicologos1.id_usuario
  AND usuarios1.tipo = 'psicologo';




select 


DROP table v_psicologo;

DROP VIEW nome_da_view;



select * from v_pacientes;

select * from v_psicologo;

SHOW FULL TABLES WHERE Table_type = 'VIEW';


DROP VIEW v_psicologo;

CREATE OR REPLACE VIEW v_usuarios AS
SELECT 
    id_usuario,
    nome_pessoa,
    TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) AS idade,
    sexo,
    cpf,
    email,
    telefone,
    endereco,
    tipo,
    criado_em
FROM usuarios1;

