-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: May 17, 2021 at 06:03 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `disease`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Id`, `Username`, `Password`) VALUES
(1, 'Nikita@gmail.com', '12345'),
(3, 'Nikita@gmail.com', '$2b$12$Oqq8ZivqmpYWFYr3v7LbE.4GMpKuAYCA1LiyOIwgSJ.HXgvYBvIAu'),
(4, 'Nikita@gmail.com', '$2b$12$lWKdCZIdXpY8ZZPmXeyu0OFdsVkHU8X.s9VOQv1yZEWtTdD11t0ee'),
(5, 'Nikita@gmail.com', '$2b$12$.JO2xA8o6GRNJmufyPrEV.kpfsdvcCPgXBH6W7LZjf9hkjktRNyWC'),
(6, 'Nikita@gmail.com', '$2b$12$mBIu7cshO3oOqukQbkBdueT9UmN6LIj/H/v8INPiUboEbRKzSq9pq'),
(7, 'Nikita@gmail.com', '$2b$12$Clt0IYwQBlDfRTjY1VcYcOnCiER2AbGxmr82ysnGzeqGEqIf.QfpW'),
(8, 'Nikita@gmail.com', '$2b$12$Ks1NTEEkXKcAjF9M7QoYCODp6Wv85BLH4krBBvF2Sy3VVUMcvMllW'),
(9, 'abc@gmail.com', '$2b$12$a4D9aUv1fQPtWKyytFtfqOFk/iUZA1oBArW99GXGKg6QdH5Uxe/b.'),
(10, 'Chhillar@mail.com', '$2b$12$5f1haGTRdGVo6FyAH299OulsF2w1gShv2lTEqW4dL2EhUbczZ.4pe'),
(11, 'Chhillar@mail.com', '1234'),
(12, 'Chhillar123@mail.com', '12345'),
(13, '', ''),
(14, 'Nikita123@gmail.com', '123'),
(15, 'Nikita456@gmail.com', '123456');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
