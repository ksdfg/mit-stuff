-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: company
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `department` (
  `Name` varchar(30) DEFAULT NULL,
  `DNo` int(11) NOT NULL,
  `MgrSSN` int(11) DEFAULT NULL,
  `SDate` date DEFAULT NULL,
  PRIMARY KEY (`DNo`),
  KEY `fk_mgr` (`MgrSSN`),
  CONSTRAINT `fk_mgr` FOREIGN KEY (`MgrSSN`) REFERENCES `employee` (`SSN`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('Marketing',10321,104,'2019-04-15'),('R & D',10322,107,'2019-04-12'),('Internal Affairs',10323,103,'2019-03-19'),('Planning',10324,110,'2019-06-04'),('Human Resources',10325,101,'2019-05-04');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependent`
--

DROP TABLE IF EXISTS `dependent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dependent` (
  `Name` varchar(20) NOT NULL,
  `Sex` char(1) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Relation` varchar(20) DEFAULT NULL,
  `SSN` int(11) NOT NULL,
  KEY `fk_ssn` (`SSN`),
  CONSTRAINT `fk_ssn` FOREIGN KEY (`SSN`) REFERENCES `employee` (`SSN`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependent`
--

LOCK TABLES `dependent` WRITE;
/*!40000 ALTER TABLE `dependent` DISABLE KEYS */;
INSERT INTO `dependent` VALUES ('Tanjiro','m','1987-07-14','Brother',110),('Funicia','f','1993-05-20','Sister',109),('Ivan','m','1960-01-21','Father',108),('Lucy','f','1967-10-31','Mother',107),('Kanata','m','1990-12-31','Husband',107),('Charles','m','1995-09-25','Cousin',106),('Maria','f','1942-11-12','Grandmother',105),('Hermione','f','1991-10-03','Wife',102);
/*!40000 ALTER TABLE `dependent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deptloc`
--

DROP TABLE IF EXISTS `deptloc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `deptloc` (
  `DNo` int(11) NOT NULL,
  `Location` varchar(60) NOT NULL,
  PRIMARY KEY (`DNo`,`Location`),
  CONSTRAINT `fk_deptloc_dno` FOREIGN KEY (`DNo`) REFERENCES `department` (`DNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deptloc`
--

LOCK TABLES `deptloc` WRITE;
/*!40000 ALTER TABLE `deptloc` DISABLE KEYS */;
INSERT INTO `deptloc` VALUES (10321,'Naples'),(10321,'New Jersey'),(10322,'Naples'),(10322,'New Jersey'),(10323,'Boston'),(10324,'Naples'),(10324,'Petropavlovsk-Kamchatsky'),(10325,'Brooklyn'),(10325,'Mumbai');
/*!40000 ALTER TABLE `deptloc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `employee` (
  `SSN` int(11) NOT NULL,
  `Name` varchar(10) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `StDate` date DEFAULT NULL,
  `Address` varchar(60) DEFAULT NULL,
  `Salary` float(10,2) DEFAULT NULL,
  `Sex` char(1) DEFAULT NULL,
  `DNo` int(11) DEFAULT NULL,
  `SupSSN` int(11) DEFAULT NULL,
  PRIMARY KEY (`SSN`),
  KEY `fk_emp_dno` (`DNo`),
  KEY `fk_supervisor` (`SupSSN`),
  CONSTRAINT `fk_emp_dno` FOREIGN KEY (`DNo`) REFERENCES `department` (`DNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_supervisor` FOREIGN KEY (`SupSSN`) REFERENCES `employee` (`SSN`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (101,'Dick','1994-04-18','2014-09-28','Jhopdi #3, Galli #5, Block #4, Dharavi, Mumbai',90341.82,'m',10325,106),(102,'Harry','1991-10-02','2014-05-04','#1, McPa Society Wing B5, Naples',100460.81,'m',10321,108),(103,'Maurilio','1994-11-06','2013-06-18','#3, Slaviola Enclave, Boston',9376.33,'m',10323,101),(104,'Tom','1989-06-03','2017-08-15','#9, Astra Residency, New Jersey',21150.18,'m',10321,106),(105,'Luca','1991-02-18','2014-01-25','#9, Astra Residency, New Jersey',89509.81,'f',10322,101),(106,'Aries','1992-02-10','2012-01-08','#3, Slaviola Enclave, Boston',128259.23,'f',10323,108),(107,'Yunhua','1990-02-03','2012-10-07','#1, McPa Society Wing B5, Naples',187912.86,'f',10322,109),(108,'Igor','1990-07-26','2012-08-18','#69, Spasibo Society Wing 420, Petropavlovsk-Kamchatsky',92163.12,'m',10324,105),(109,'Quitterie','1987-05-29','2013-03-28','#23, Winston Street, Brooklyn',119826.50,'f',10325,102),(110,'Nezuko','1988-12-28','2014-12-15','#1, McPa Society Wing B5, Naples',85413.35,'f',10324,107);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `project` (
  `PName` varchar(20) DEFAULT NULL,
  `PNo` int(11) NOT NULL,
  `Location` varchar(60) DEFAULT NULL,
  `DNo` int(11) DEFAULT NULL,
  PRIMARY KEY (`PNo`),
  KEY `fk_project_dno` (`DNo`),
  CONSTRAINT `fk_project_dno` FOREIGN KEY (`DNo`) REFERENCES `department` (`DNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES ('Senku 4',1,'New Jersey',10322),('SpaceX Integration',2,'Naples',10321),('Half Life 3',3,'Naples',10322),('Tax Evasion',4,'Boston',10323),('Consumer Survey',5,'Naples',10324),('Recruitment Drive',6,'Mumbai',10325),('Annual Budget',7,'Petropavlovsk-Kamchatsky',10324),('Harassment',8,'Brooklyn',10325),('Bribery',9,'Boston',10323),('Ad Campaign',10,'New Jersey',10321);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works`
--

DROP TABLE IF EXISTS `works`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `works` (
  `SSN` int(11) NOT NULL,
  `PNo` int(11) NOT NULL,
  `Hours` int(11) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`PNo`),
  KEY `fk_work_pno` (`PNo`),
  CONSTRAINT `fk_work_pno` FOREIGN KEY (`PNo`) REFERENCES `project` (`PNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_work_ssn` FOREIGN KEY (`SSN`) REFERENCES `employee` (`SSN`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works`
--

LOCK TABLES `works` WRITE;
/*!40000 ALTER TABLE `works` DISABLE KEYS */;
INSERT INTO `works` VALUES (101,6,47),(102,2,32),(103,9,39),(104,10,32),(105,1,35),(106,4,32),(107,3,40),(108,7,50),(109,8,29),(110,5,30);
/*!40000 ALTER TABLE `works` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-09 11:32:39
