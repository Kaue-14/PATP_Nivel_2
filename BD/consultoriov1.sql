-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 20/11/2024 às 00:42
-- Versão do servidor: 8.0.39
-- Versão do PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `consultoriov1`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `agendamentos1`
--

DROP TABLE IF EXISTS `agendamentos1`;
CREATE TABLE IF NOT EXISTS `agendamentos1` (
  `id_agendamento` int NOT NULL AUTO_INCREMENT,
  `id_paciente` int NOT NULL,
  `id_psicologo` int NOT NULL,
  `status` enum('agendado','cancelado','concluído') DEFAULT 'agendado',
  `observacoes` text,
  `data` date NOT NULL,
  `hora` time NOT NULL,
  PRIMARY KEY (`id_agendamento`),
  KEY `fk_agendamento_paciente` (`id_paciente`),
  KEY `fk_agendamento_psicologo` (`id_psicologo`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `agendamentos1`
--

INSERT INTO `agendamentos1` (`id_agendamento`, `id_paciente`, `id_psicologo`, `status`, `observacoes`, `data`, `hora`) VALUES
(1, 1, 1, 'agendado', 'Primeira consulta', '2024-12-04', '08:00:00'),
(41, 2, 1, 'agendado', 'teste', '2024-11-26', '11:00:00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pacientes1`
--

DROP TABLE IF EXISTS `pacientes1`;
CREATE TABLE IF NOT EXISTS `pacientes1` (
  `id_paciente` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `historico_consultas` text,
  `possui_alergias` enum('sim','nao') DEFAULT 'nao',
  `descricao_alergias` text,
  `possui_plano_saude` enum('sim','nao') DEFAULT 'nao',
  PRIMARY KEY (`id_paciente`),
  KEY `fk_pacientes_usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `pacientes1`
--

INSERT INTO `pacientes1` (`id_paciente`, `id_usuario`, `historico_consultas`, `possui_alergias`, `descricao_alergias`, `possui_plano_saude`) VALUES
(1, 1, 'Consulta inicial em 2024', 'nao', '', 'sim'),
(2, 2, 'Histórico limpo', 'nao', '', 'nao');

-- --------------------------------------------------------

--
-- Estrutura para tabela `psicologos1`
--

DROP TABLE IF EXISTS `psicologos1`;
CREATE TABLE IF NOT EXISTS `psicologos1` (
  `id_psicologo` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `especialidade` varchar(100) DEFAULT NULL,
  `registro_profissional` varchar(20) DEFAULT NULL,
  `experiencia` text,
  `horario_atendimento` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_psicologo`),
  KEY `fk_psicologos_usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `psicologos1`
--

INSERT INTO `psicologos1` (`id_psicologo`, `id_usuario`, `especialidade`, `registro_profissional`, `experiencia`, `horario_atendimento`) VALUES
(1, 3, 'Psicologia Clínica', 'CRP123456', '10 anos de experiência', 'Seg-Sex 08:00-18:00');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios1`
--

DROP TABLE IF EXISTS `usuarios1`;
CREATE TABLE IF NOT EXISTS `usuarios1` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome_pessoa` varchar(100) NOT NULL,
  `data_nascimento` date NOT NULL,
  `sexo` enum('M','F') NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` varchar(255) NOT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `tipo` enum('admin','psicologo','paciente') DEFAULT 'paciente',
  `criado_em` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_psicologo` int DEFAULT NULL,
  `id_paciente` int DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `cpf` (`cpf`),
  KEY `fk_usuarios_psicologo` (`id_psicologo`),
  KEY `fk_usuarios_paciente` (`id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `usuarios1`
--

INSERT INTO `usuarios1` (`id_usuario`, `nome_pessoa`, `data_nascimento`, `sexo`, `cpf`, `email`, `senha`, `telefone`, `endereco`, `tipo`, `criado_em`, `id_psicologo`, `id_paciente`) VALUES
(1, 'Maria Souza', '1992-06-15', 'F', '98765432100', 'maria.souza@gmail.com', 'senha_segura', '054987654321', 'Rua Paciente, 45', 'paciente', '2024-11-12 22:05:35', NULL, 1),
(2, 'Carlos Mendes', '1985-08-20', 'M', '01234567890', 'carlos.mendes@gmail.com', 'carlos123', '054912345678', 'Rua Clínica, 98', 'paciente', '2024-11-12 22:05:35', NULL, 2),
(3, 'Dr. João Silva', '1980-03-10', 'M', '1234567019', 'joao.silva@gmail.com', 'senha_hash', '054998765432', 'Rua Psicologia, 123', 'psicologo', '2024-11-12 22:05:35', 1, NULL),
(23, '', '2024-11-26', 'F', '', '', '', '', '', 'psicologo', '2024-11-20 00:32:41', NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `v_pacientes`
-- (Veja abaixo para a visão atual)
--
DROP VIEW IF EXISTS `v_pacientes`;
CREATE TABLE IF NOT EXISTS `v_pacientes` (
`id_usuario` int
,`nome_pessoa` varchar(100)
,`idade` bigint
,`sexo` enum('M','F')
,`cpf` varchar(11)
,`email` varchar(100)
,`telefone` varchar(15)
,`endereco` varchar(255)
,`tipo` enum('admin','psicologo','paciente')
,`criado_em` timestamp
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `v_psicologo`
-- (Veja abaixo para a visão atual)
--
DROP VIEW IF EXISTS `v_psicologo`;
CREATE TABLE IF NOT EXISTS `v_psicologo` (
`id_usuario` int
,`nome_pessoa` varchar(100)
,`idade` bigint
,`sexo` enum('M','F')
,`email` varchar(100)
,`telefone` varchar(15)
,`cpf` varchar(11)
,`endereco` varchar(255)
,`id_psicologo` int
,`especialidade` varchar(100)
,`registro_profissional` varchar(20)
,`experiencia` text
,`horario_atendimento` varchar(255)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `v_usuarios`
-- (Veja abaixo para a visão atual)
--
DROP VIEW IF EXISTS `v_usuarios`;
CREATE TABLE IF NOT EXISTS `v_usuarios` (
`id_usuario` int
,`nome_pessoa` varchar(100)
,`idade` bigint
,`sexo` enum('M','F')
,`cpf` varchar(11)
,`email` varchar(100)
,`telefone` varchar(15)
,`endereco` varchar(255)
,`tipo` enum('admin','psicologo','paciente')
,`criado_em` timestamp
);

-- --------------------------------------------------------

--
-- Estrutura para view `v_pacientes`
--
DROP TABLE IF EXISTS `v_pacientes`;

DROP VIEW IF EXISTS `v_pacientes`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_pacientes`  AS SELECT `usuarios1`.`id_usuario` AS `id_usuario`, `usuarios1`.`nome_pessoa` AS `nome_pessoa`, timestampdiff(YEAR,`usuarios1`.`data_nascimento`,curdate()) AS `idade`, `usuarios1`.`sexo` AS `sexo`, `usuarios1`.`cpf` AS `cpf`, `usuarios1`.`email` AS `email`, `usuarios1`.`telefone` AS `telefone`, `usuarios1`.`endereco` AS `endereco`, `usuarios1`.`tipo` AS `tipo`, `usuarios1`.`criado_em` AS `criado_em` FROM `usuarios1` WHERE (`usuarios1`.`tipo` = 'paciente') ;

-- --------------------------------------------------------

--
-- Estrutura para view `v_psicologo`
--
DROP TABLE IF EXISTS `v_psicologo`;

DROP VIEW IF EXISTS `v_psicologo`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_psicologo`  AS SELECT `usuarios1`.`id_usuario` AS `id_usuario`, `usuarios1`.`nome_pessoa` AS `nome_pessoa`, timestampdiff(YEAR,`usuarios1`.`data_nascimento`,curdate()) AS `idade`, `usuarios1`.`sexo` AS `sexo`, `usuarios1`.`email` AS `email`, `usuarios1`.`telefone` AS `telefone`, `usuarios1`.`cpf` AS `cpf`, `usuarios1`.`endereco` AS `endereco`, `psicologos1`.`id_psicologo` AS `id_psicologo`, `psicologos1`.`especialidade` AS `especialidade`, `psicologos1`.`registro_profissional` AS `registro_profissional`, `psicologos1`.`experiencia` AS `experiencia`, `psicologos1`.`horario_atendimento` AS `horario_atendimento` FROM (`usuarios1` join `psicologos1`) WHERE ((`usuarios1`.`id_usuario` = `psicologos1`.`id_usuario`) AND (`usuarios1`.`tipo` = 'psicologo')) ;

-- --------------------------------------------------------

--
-- Estrutura para view `v_usuarios`
--
DROP TABLE IF EXISTS `v_usuarios`;

DROP VIEW IF EXISTS `v_usuarios`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_usuarios`  AS SELECT `usuarios1`.`id_usuario` AS `id_usuario`, `usuarios1`.`nome_pessoa` AS `nome_pessoa`, timestampdiff(YEAR,`usuarios1`.`data_nascimento`,curdate()) AS `idade`, `usuarios1`.`sexo` AS `sexo`, `usuarios1`.`cpf` AS `cpf`, `usuarios1`.`email` AS `email`, `usuarios1`.`telefone` AS `telefone`, `usuarios1`.`endereco` AS `endereco`, `usuarios1`.`tipo` AS `tipo`, `usuarios1`.`criado_em` AS `criado_em` FROM `usuarios1` ;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `agendamentos1`
--
ALTER TABLE `agendamentos1`
  ADD CONSTRAINT `fk_agendamento_paciente` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes1` (`id_paciente`),
  ADD CONSTRAINT `fk_agendamento_psicologo` FOREIGN KEY (`id_psicologo`) REFERENCES `psicologos1` (`id_psicologo`);

--
-- Restrições para tabelas `pacientes1`
--
ALTER TABLE `pacientes1`
  ADD CONSTRAINT `fk_pacientes_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios1` (`id_usuario`);

--
-- Restrições para tabelas `psicologos1`
--
ALTER TABLE `psicologos1`
  ADD CONSTRAINT `fk_psicologos_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios1` (`id_usuario`);

--
-- Restrições para tabelas `usuarios1`
--
ALTER TABLE `usuarios1`
  ADD CONSTRAINT `fk_usuarios_paciente` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes1` (`id_paciente`),
  ADD CONSTRAINT `fk_usuarios_psicologo` FOREIGN KEY (`id_psicologo`) REFERENCES `psicologos1` (`id_psicologo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
