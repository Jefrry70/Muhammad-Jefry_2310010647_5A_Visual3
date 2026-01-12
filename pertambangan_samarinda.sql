-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2026 at 01:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pertambangan_samarinda`
--

-- --------------------------------------------------------

--
-- Table structure for table `desa`
--

CREATE TABLE `desa` (
  `id_desa` int(11) NOT NULL,
  `provinsi` varchar(100) NOT NULL,
  `kabkot` varchar(100) NOT NULL,
  `kecamatan` varchar(100) NOT NULL,
  `desa` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `desa`
--

INSERT INTO `desa` (`id_desa`, `provinsi`, `kabkot`, `kecamatan`, `desa`) VALUES
(1, 'Kalimantan Selatan', 'Banjarmasin', 'Banjar Indah', 'Mantuil'),
(2, 'Kalimantan Tengah', 'Palangkaraya', 'Palangkaraya', 'Bangka Belitung'),
(3, 'Kalimantan Selatan', 'Marabahan', 'TelagaBiru', 'Sungai Danau');

-- --------------------------------------------------------

--
-- Table structure for table `iup_samarinda`
--

CREATE TABLE `iup_samarinda` (
  `id_iup` int(11) NOT NULL,
  `nama_usaha` varchar(100) NOT NULL,
  `komoditas` varchar(50) NOT NULL,
  `luas_sk` double NOT NULL,
  `id_desa` int(11) DEFAULT NULL,
  `id_sungai_besar` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pemukiman`
--

CREATE TABLE `pemukiman` (
  `id_pemukiman` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `kode` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sungai_besar`
--

CREATE TABLE `sungai_besar` (
  `id_sungai_besar` int(11) NOT NULL,
  `nama_sungai` varchar(100) NOT NULL,
  `kode_unsur` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `desa`
--
ALTER TABLE `desa`
  ADD PRIMARY KEY (`id_desa`);

--
-- Indexes for table `iup_samarinda`
--
ALTER TABLE `iup_samarinda`
  ADD PRIMARY KEY (`id_iup`),
  ADD KEY `id_desa` (`id_desa`),
  ADD KEY `id_sungai_besar` (`id_sungai_besar`);

--
-- Indexes for table `pemukiman`
--
ALTER TABLE `pemukiman`
  ADD PRIMARY KEY (`id_pemukiman`);

--
-- Indexes for table `sungai_besar`
--
ALTER TABLE `sungai_besar`
  ADD PRIMARY KEY (`id_sungai_besar`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `desa`
--
ALTER TABLE `desa`
  MODIFY `id_desa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `iup_samarinda`
--
ALTER TABLE `iup_samarinda`
  MODIFY `id_iup` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pemukiman`
--
ALTER TABLE `pemukiman`
  MODIFY `id_pemukiman` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sungai_besar`
--
ALTER TABLE `sungai_besar`
  MODIFY `id_sungai_besar` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `iup_samarinda`
--
ALTER TABLE `iup_samarinda`
  ADD CONSTRAINT `iup_samarinda_ibfk_1` FOREIGN KEY (`id_desa`) REFERENCES `desa` (`id_desa`),
  ADD CONSTRAINT `iup_samarinda_ibfk_2` FOREIGN KEY (`id_sungai_besar`) REFERENCES `sungai_besar` (`id_sungai_besar`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
