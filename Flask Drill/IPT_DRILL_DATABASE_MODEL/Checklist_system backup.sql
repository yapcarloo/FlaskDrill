-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema checklist_system
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema checklist_system
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `checklist_system` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `checklist_system` ;

-- -----------------------------------------------------
-- Table `checklist_system`.`salesmans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `checklist_system`.`salesmans` (
  `salesman_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NULL DEFAULT NULL,
  `commission` DECIMAL(5,2) NULL DEFAULT NULL,
  PRIMARY KEY (`salesman_id`),
  UNIQUE INDEX `first_name` (`first_name` ASC, `last_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `checklist_system`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `checklist_system`.`orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `purchase_amount` DECIMAL(10,2) NOT NULL,
  `order_date` DATE NOT NULL,
  `customer_id` INT NOT NULL,
  `salesman_id` INT NOT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `orders_id_idx` (`salesman_id` ASC) VISIBLE,
  INDEX `orders_id2_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `orders_id`
    FOREIGN KEY (`salesman_id`)
    REFERENCES `checklist_system`.`salesmans` (`salesman_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `checklist_system`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `checklist_system`.`customer` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`customer_id`),
  CONSTRAINT `customer_ID`
    FOREIGN KEY (`customer_id`)
    REFERENCES `checklist_system`.`orders` (`order_id`),
  CONSTRAINT `customerID`
    FOREIGN KEY (`customer_id`)
    REFERENCES `checklist_system`.`salesmans` (`salesman_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
