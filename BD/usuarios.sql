-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 04/10/2024 às 00:24
-- Versão do servidor: 8.3.0
-- Versão do PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banco_de_usuarios`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) NOT NULL,
  `data_nascimento` date NOT NULL,
  `sexo` enum('M','F') NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` varchar(255) NOT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `categoria` enum('admin','Psicólogo(a)','Paciente') DEFAULT 'Paciente',
  `criado_em` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `cpf` (`cpf`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nome`, `data_nascimento`, `sexo`, `cpf`, `email`, `senha`, `telefone`, `endereco`, `categoria`, `criado_em`) VALUES
(1, 'admin', '2000-01-01', 'F', '00000000000', 'admin@gmail.com', 'admin', '00000000000', 'Rua admin, 00', 'admin', '2024-10-03 22:37:19'),
(2, '', '2000-01-01', 'M', '', '', '', '', '', 'admin', '2024-10-03 22:38:15'),
(3, 'Kauê Gabriel Magarin', '2005-12-14', 'M', '02629634000', 'kauegabriel815@gmail.com', 'gabriel714', '54 99602-0056', 'Rua Alfredo Augusto Koche, ND', 'Psicólogo(a)', '2024-10-04 00:02:10');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
