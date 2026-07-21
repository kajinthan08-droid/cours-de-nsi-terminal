-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Modifié le :  Jeu 04 Octobre 2018 à 10:39
-- Version du serveur :  10.1.26-MariaDB-0+deb9u1
-- Version de PHP :  7.0.19-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+02:00";

--
-- Base de données :  scolaire
--

-- --------------------------------------------------------

--
-- Structure de la table CLASSE
--

DROP TABLE IF EXISTS CLASSE;
CREATE TABLE CLASSE (
  code varchar(7) NOT NULL,
  niveau char(1) NOT NULL,
  section varchar(4) DEFAULT NULL,
  PRIMARY KEY (code)
) ENGINE=InnoDB;

--
-- Contenu de la table CLASSE
--

INSERT INTO CLASSE (code, niveau, section) VALUES
('TSTMG1', 'T', 'STMG'),
('TSTMG2', 'T', 'STMG'),
('TS', 'T', 'S'),
('TL', 'T', 'L'),
('TES', 'T', 'ES'),
('1ES', '1', 'ES'),
('1L', '1', 'L'),
('1S', '1', 'S'),
('1STI2D', '1', 'STI2D'),
('1STMG1', '1', 'STMG'),
('1STMG2', '1', 'STMG'),
('TSTI2D', 'T', 'STI2D'),
('2nd1', '2', NULL),
('2nd2', '2', NULL),
('2nd3', '2', NULL),
('2nd4', '2', NULL),
('2nd5', '2', NULL),
('2nd6', '2', NULL);

-- --------------------------------------------------------

--
-- Structure de la table ELEVE
--

DROP TABLE IF EXISTS ELEVE;
CREATE TABLE ELEVE (
  num int NOT NULL,
  nom varchar(30) NOT NULL,
  prenom varchar(30) NOT NULL,
  dateNaiss date DEFAULT NULL,
  sexe char(1) DEFAULT NULL,
  codeClasse varchar(7) DEFAULT NULL,
  PRIMARY KEY (num)
) ENGINE=InnoDB;

--
-- Contenu de la table ELEVE
--

INSERT INTO ELEVE (num, nom, prenom, dateNaiss, sexe, codeClasse) VALUES
(1, 'Hochon', 'Paul','2001-02-23','M','TSTI2D'),
(2, 'Ui', 'Arthuro','2002-06-15','M','1ES'),
(3, 'Johnson', 'Jeremia','2003-10-17','M','2nd2'),
(4, 'Blueberry', 'Mike','2003-03-27','M','2nd2'),
(5, 'Livingstone', 'Johnattan','2000-08-22','M','TSTMG1'),
(6, 'Troll', 'Moumine','2001-02-28','F','TSTMG1'),
(7, 'Pavlova', 'Jasmine','2001-05-05','F','TSTMG1'),
(8, 'Baker', 'Norma-Jean','2001-10-08','F','TSTMG1'),
(9, 'Joplin', 'Janis','2001-09-19','F','TSTI2D');

-- --------------------------------------------------------

--
-- Structure de la table ENSEIGNEMENT
--

DROP TABLE IF EXISTS ENSEIGNEMENT;
CREATE TABLE ENSEIGNEMENT (
  numProf int(11) NOT NULL,
  codeClasse varchar(7) NOT NULL,
  nbHeures int(11) NOT NULL,
  PRIMARY KEY (numProf,codeClasse)
) ENGINE=InnoDB;

--
-- Contenu de la table ENSEIGNEMENT
--

INSERT INTO ENSEIGNEMENT (numProf, codeClasse, nbHeures) VALUES
(1, '2nd2', 3),
(1, 'TS', 7),
(1, 'TSTMG1', 4),
(7, 'TSTMG1', 6),
(5, '2nd2', 3),
(5, '2nd1', 3),
(5, 'TSTMG1', 4),
(5, 'TS', 4),
(5, '1STMG1', 4),
(6, '2nd2', 3),
(6, '2nd1', 3),
(2, 'TSTMG1', 4);

-- --------------------------------------------------------

--
-- Structure de la table PROFESSEUR
--

DROP TABLE IF EXISTS PROFESSEUR;
CREATE TABLE PROFESSEUR (
  num int NOT NULL AUTO_INCREMENT,
  nom varchar(30) NOT NULL,
  prenom varchar(30) DEFAULT NULL,
  discipline varchar(30) DEFAULT NULL,
  PRIMARY KEY (num)
) ENGINE=InnoDB;

--
-- Contenu de la table PROFESSEUR
--

INSERT INTO PROFESSEUR (num, nom, prenom, discipline) VALUES
(1, 'Munn', 'Homir', 'Mathématiques'),
(2, 'Corleone', 'Vito', 'EPS'),
(3, 'Stark', 'Catelyn', 'Physique-Chimie'),
(4, 'Targaryen', 'Daeneris', 'Français'),
(5, 'Lannister', 'Jaime', 'Anglais'),
(6, 'Snow', 'Jon', 'Espagnol'),
(7, 'Mordane', 'Septa', 'SIG'),
(8, 'Arryn', 'Lysa', 'Itech'),
(9, 'Frey', 'Walder', 'Economie');


