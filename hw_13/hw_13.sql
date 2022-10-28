-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: my_db_hw13
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `classroom`
--

DROP TABLE IF EXISTS `classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classroom` (
  `id` int DEFAULT NULL,
  `classroom number` varchar(50) DEFAULT NULL,
  `floor` mediumint NOT NULL,
  `academic subject` varchar(50) NOT NULL,
  `student group` varchar(50) NOT NULL,
  KEY `fk_student_group` (`student group`),
  CONSTRAINT `fk_student_group` FOREIGN KEY (`student group`) REFERENCES `students` (`student group`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classroom`
--

LOCK TABLES `classroom` WRITE;
/*!40000 ALTER TABLE `classroom` DISABLE KEYS */;
INSERT INTO `classroom` VALUES (1,'202',2,'biology','1a'),(2,'302',3,'chemistry','2b'),(3,'402',4,'mathematics','3c');
/*!40000 ALTER TABLE `classroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `student group` varchar(50) NOT NULL,
  `academic subject` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_group` (`student group`),
  KEY `index_subject` (`academic subject`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Dima','Orlov','1a','biology'),(2,'Karl','Mishkin','1a','biology'),(3,'Oswald','Spengler','1a','biology'),(4,'Ivan','Ivanov','1a','biology'),(5,'Petr','Petrov','1a','biology'),(6,'Zina','Sokolova','2b','chemistry'),(7,'Ira','Ivanova','2b','chemistry'),(8,'Anna','Nabokova','2b','chemistry'),(9,'Anna','Nabokova','3c','mathematics'),(10,'Natasha','Zhychkova','3c','mathematics'),(11,'Igor','Sidorov','3c','mathematics'),(12,'Ivan','Volkov','3c','mathematics');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students on the course`
--

DROP TABLE IF EXISTS `students on the course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students on the course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `student group` varchar(50) NOT NULL,
  `assessment` mediumint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_student_group_in_course` (`student group`),
  CONSTRAINT `fk_student_group_in_course` FOREIGN KEY (`student group`) REFERENCES `students` (`student group`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_student_id` FOREIGN KEY (`id`) REFERENCES `students` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students on the course`
--

LOCK TABLES `students on the course` WRITE;
/*!40000 ALTER TABLE `students on the course` DISABLE KEYS */;
INSERT INTO `students on the course` VALUES (1,'Dima','Orlov','1a',9),(2,'Karl','Mishkin','1a',9),(3,'Oswald','Spengler','1a',9),(4,'Ivan','Ivanov','1a',9),(5,'Petr','Petrov','1a',10),(6,'Zina','Sokolova','2b',9),(7,'Ira','Ivanova','2b',9),(8,'Anna','Nabokova','2b',8),(9,'Anna','Drozdova','3c',9),(10,'Natasha','Zhychkova','3c',10),(11,'Igor','Sidorov','3c',8),(12,'Ivan','Volkov','3c',8);
/*!40000 ALTER TABLE `students on the course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `academic subject` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subject` (`academic subject`),
  CONSTRAINT `fk_subject` FOREIGN KEY (`academic subject`) REFERENCES `students` (`academic subject`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'Dmitri','Mendeleev','chemistry'),(2,'Carl','Linnaeus','biology'),(3,'Carl','Gauss','mathematics');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-26  1:04:21
