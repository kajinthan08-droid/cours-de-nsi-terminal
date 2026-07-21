-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Modifié le :  Dim 07 Octobre 2018 à 16:16
-- Version du serveur :  10.1.26-MariaDB-0+deb9u1
-- Version de PHP :  7.0.19-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de données :  Commerciale
--

-- --------------------------------------------------------

--
-- Structure de la table FACTURE
--

CREATE TABLE FACTURE (
  numero int NOT NULL,
  dateFacture date DEFAULT NULL,
  PRIMARY KEY (numero)
) ENGINE=InnoDB;

--
-- Contenu de la table FACTURE
--

INSERT INTO FACTURE (numero, dateFacture) VALUES
(1, '2017-11-06'),
(2, '2017-11-08'),
(3, '2017-11-15'),
(4, '2017-11-17'),
(5, '2017-12-06');

-- --------------------------------------------------------

--
-- Structure de la table PRODUIT
--

CREATE TABLE PRODUIT (
  reference int NOT NULL,
  designation varchar(50) DEFAULT NULL,
  prix decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (reference)
) ENGINE=InnoDB;

--
-- Contenu de la table PRODUIT
--

INSERT INTO PRODUIT (reference, designation, prix) VALUES
(1, 'Ordinateur HP DeskPro 2510', '150.00'),
(2, 'Ordinateur Sony Vaio ZM25', '230.00'),
(3, 'Switch DLink GS108', '30.00'),
(4, 'Câble RJ45 10m Blanc', '22.50'),
(5, 'Disque Dur SATA3 1To', '80.00'),
(6, 'Câble RJ45 2m Blanc', '4.50'),
(7, 'Clef USB 3.0 16Go', '24.80'),
(8, 'Câble VGA M/M 2m', '15.50'),
(9, 'Câble HDMI M/M 2m', '26.80'),
(10, 'Boitier convertisseur HDMI/VGA', '41.20');

-- --------------------------------------------------------

--
-- Structure de la table PRODUITFACTURE
--

CREATE TABLE PRODUITFACTURE (
  numFacture int NOT NULL,
  numProduit int NOT NULL,
  quantite int DEFAULT NULL,
  PRIMARY KEY (numFacture,numProduit),
  FOREIGN KEY (numProduit) REFERENCES PRODUIT(reference),
  FOREIGN KEY (numFacture) REFERENCES FACTURE(numero)
) ENGINE=InnoDB;

--
-- Contenu de la table PRODUITFACTURE
--

INSERT INTO PRODUITFACTURE (numFacture, numProduit, quantite) VALUES
(1, 3, 1),
(1, 4, 1),
(1, 6, 3),
(2, 1, 1),
(3, 5, 2),
(4, 9, 1),
(4, 10, 1),
(5, 7, 25);



-- --------------------------------------------------------

--
-- Structure de la table PRODUITFACTURE_V2
--

-- CREATE TABLE PRODUITFACTURE_V2 (
--   numFacture int NOT NULL,
--   dateFacture date DEFAULT NULL,
--   numProduit int NOT NULL,
--   designation varchar(50) DEFAULT NULL,
--   prix decimal(5,2) DEFAULT NULL,
--   quantite int DEFAULT NULL,
-- ) ENGINE=InnoDB;

--
-- Contenu de la table PRODUITFACTURE_V2
--

-- INSERT INTO PRODUITFACTURE_V2 (numFacture, numProduit, quantite) VALUES
-- (1, '2017-11-06', 3, 'Switch DLink GS108', '30.00', 1),
-- (1, '2017-11-06', 4, 'Câble RJ45 10m Blanc', '22.50', 1),
-- (1, '2017-11-06', 6, 'Câble RJ45 2m Blanc', '4.50', 3),
-- (2, '2017-11-08', 1, 'Ordinateur HP DeskPro 2510', '150.00', 1),
-- (3, '2017-11-15', 5, 'Disque Dur SATA3 1To', '80.00', 2),
-- (4, '2017-11-17', 9, 'Câble HDMI M/M 2m', '26.80', 1),
-- (4, '2017-11-17', 10, 'Boitier convertisseur HDMI/VGA', '41.20', 1),
-- (5, '2017-12-06', 7, 'Clef USB 3.0 16Go', '24.80', 25);

