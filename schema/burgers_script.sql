-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema login_reg
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `login_reg` ;

-- -----------------------------------------------------
-- Schema login_reg
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_reg` DEFAULT CHARACTER SET utf8 ;
USE `login_reg` ;

-- -----------------------------------------------------
-- Table `login_reg`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `login_reg`.`burgers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`burgers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `bun` VARCHAR(255) NULL,
  `meat` VARCHAR(255) NULL,
  `calories` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_burgers_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_burgers_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `login_reg`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `login_reg`.`toppings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`toppings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `topping_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `login_reg`.`add_ons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`add_ons` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `topping_id` INT NULL,
  `burger_id` INT NULL,
  INDEX `fk_toppings_has_burgers_burgers1_idx` (`burger_id` ASC) VISIBLE,
  INDEX `fk_toppings_has_burgers_toppings1_idx` (`topping_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_toppings_has_burgers_toppings1`
    FOREIGN KEY (`topping_id`)
    REFERENCES `login_reg`.`toppings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_toppings_has_burgers_burgers1`
    FOREIGN KEY (`burger_id`)
    REFERENCES `login_reg`.`burgers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
