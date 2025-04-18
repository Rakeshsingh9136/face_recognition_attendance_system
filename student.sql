-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2025 at 12:36 PM
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
-- Database: `mydata`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `Dep` varchar(55) NOT NULL,
  `course` varchar(125) NOT NULL,
  `year` varchar(55) NOT NULL,
  `Semester` varchar(255) NOT NULL,
  `Name` varchar(75) NOT NULL,
  `division` varchar(75) NOT NULL,
  `Roll_no` varchar(125) NOT NULL,
  `Gender` varchar(35) NOT NULL,
  `DOB` varchar(45) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` varchar(35) NOT NULL,
  `addressl` varchar(240) NOT NULL,
  `teacher` varchar(75) NOT NULL,
  `photosample` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `Dep`, `course`, `year`, `Semester`, `Name`, `division`, `Roll_no`, `Gender`, `DOB`, `email`, `mobile`, `addressl`, `teacher`, `photosample`) VALUES
(1, 'TE', '2020-21', '7th', '45', 'Rakesh', 'G1', '26', 'Male', '11/12/2000', 'rakesh@gmail.com', '8400267075', 'Gr. Noida', 'abcd', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
