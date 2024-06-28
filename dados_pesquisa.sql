CREATE DATABASE pesquisa;

USE pesquisa;

CREATE TABLE participantes (
ID INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
idade INT,
sexo ENUM('M', 'F'),
estado VARCHAR(50),
escolaridade VARCHAR (100),
estado_civil VARCHAR(50),
tem_filhos BOOLEAN
);


