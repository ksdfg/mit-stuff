-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: ass4
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
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `city` (
  `city_name` varchar(20) NOT NULL,
  `population` int(11) DEFAULT NULL,
  PRIMARY KEY (`city_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES ('Aurangabad',200000),('Chennai',78000000),('Delhi',50000000),('Jahirabad',3141444),('Mumbai',40000000),('Pune',6000000),('Surat',1231231);
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customer` (
  `cust_id` int(11) NOT NULL,
  `cust_name` varchar(40) DEFAULT NULL,
  `annual_revenue` float(10,2) DEFAULT (20000),
  `cust_type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`cust_id`),
  CONSTRAINT `customer_chk_1` CHECK (((`cust_id` > 100) and (`cust_id` < 10000)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (101,'Rajesh Shah',100000.00,'Speciality Wholesaler'),(153,'Sanjay Surana',3400000.00,'Retailer'),(184,'Komal Malviya',96000.00,'Drop Ship Wholesalers'),(200,'Kuber Khanna',20083.00,'Drop Ship Wholesalers'),(599,'Nitesh Jagdale',7800.00,'Retailer'),(785,'Saurabh Deshpande',500000.00,'On-line Wholesaler '),(986,'Satish Kumar',30000.00,'Retailer');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipment`
--

DROP TABLE IF EXISTS `shipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `shipment` (
  `shipment_id` int(11) NOT NULL,
  `cust_id` int(11) DEFAULT NULL,
  `weight` float(6,2) DEFAULT '10.00',
  `truck_id` int(11) DEFAULT NULL,
  `destination` varchar(20) DEFAULT NULL,
  `ship_date` date DEFAULT NULL,
  PRIMARY KEY (`shipment_id`),
  KEY `fk_cust` (`cust_id`),
  KEY `fk_truck` (`truck_id`),
  KEY `fk_dest` (`destination`),
  CONSTRAINT `fk_cust` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`),
  CONSTRAINT `fk_dest` FOREIGN KEY (`destination`) REFERENCES `city` (`city_name`),
  CONSTRAINT `fk_truck` FOREIGN KEY (`truck_id`) REFERENCES `truck` (`truck_id`),
  CONSTRAINT `shipment_chk_1` CHECK ((`weight` < 1000))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipment`
--

LOCK TABLES `shipment` WRITE;
/*!40000 ALTER TABLE `shipment` DISABLE KEYS */;
INSERT INTO `shipment` VALUES (23463434,101,200.00,10,'Pune','2012-04-10'),(31273124,599,345.00,12,'Pune','2010-01-09'),(39639066,599,180.00,12,'Pune','2007-12-02'),(42323434,184,534.00,13,'Pune','2015-03-15'),(58259259,153,20.00,11,'Mumbai','2016-05-31'),(64574652,184,34.45,10,'Pune','2015-03-15'),(69045867,785,896.00,10,'Pune','2016-11-30'),(72134714,184,23.40,13,'Chennai','2017-09-11'),(79840975,101,345.00,11,'Aurangabad','2005-06-22'),(86248124,785,313.34,11,'Pune','2010-01-09'),(86487655,599,14.56,12,'Chennai','2013-05-25'),(94509435,599,312.45,10,'Delhi','2010-02-27'),(342138414,785,180.00,11,'Mumbai','2013-05-25'),(414146148,101,180.00,10,'Mumbai','2015-03-15'),(414914814,153,896.00,11,'Pune','2010-02-27');
/*!40000 ALTER TABLE `shipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `truck`
--

DROP TABLE IF EXISTS `truck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `truck` (
  `truck_id` int(11) NOT NULL,
  `driver_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`truck_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `truck`
--

LOCK TABLES `truck` WRITE;
/*!40000 ALTER TABLE `truck` DISABLE KEYS */;
INSERT INTO `truck` VALUES (10,'Allen'),(11,'Sham'),(12,'Ram'),(13,'Sagar');
/*!40000 ALTER TABLE `truck` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 13:16:53
