-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `backproject` DEFAULT CHARACTER SET utf8 ;
USE `backproject` ;

-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `backproject`.`user` (
  `id_user` INT NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `email_us` VARCHAR(45) NOT NULL,
  `password_user` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_user`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `backproject`.`books` (
  `id_books` INT NOT NULL,
  `Nome_livro` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_books`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`livros_favoritos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `backproject`.`livros_favoritos` (
  `user_id_user` INT NOT NULL,
  `books_id_books` INT NOT NULL,
  PRIMARY KEY (`user_id_user`, `books_id_books`),
  INDEX `fk_user_has_books_books1_idx` (`books_id_books` ASC) VISIBLE,
  INDEX `fk_user_has_books_user_idx` (`user_id_user` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_books_user`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `backproject`.`user` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_books_books1`
    FOREIGN KEY (`books_id_books`)
    REFERENCES `backproject`.`books` (`id_books`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

select * from user;
 show tables;
ALTER TABLE books
ADD COLUMN nome_autor VARCHAR(255) AFTER nome_livro;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
