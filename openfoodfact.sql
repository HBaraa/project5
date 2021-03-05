SET NAMES utf8;
DROP DATABASE IF EXISTS openfoodfacts;
CREATE DATABASE openfoodfact;
USE openfoodfact;
CREATE TABLE category(
	id INTEGER UNSIGNED AUTO_INCREMENT,
	name VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
	)ENGINE=InnoDB;
CREATE TABLE Category_product(
	id INTEGER UNSIGNED AUTO_INCREMENT,
    category_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    PRIMARY KEY(id)
    )ENGINE=InnoDB;
CREATE TABLE product(
	id INTEGER UNSIGNED AUTO_INCREMENT,
	nutriscore_id INTEGER NOT NULL,
	name VARCHAR(400) NOT NULL,   
	code VARCHAR(100) NOT NULL,
    description VARCHAR(800) NOT NULL,
    url VARCHAR(400) NOT NULL,
    store VARCHAR(400) NOT NULL,
	PRIMARY KEY(id)
	)ENGINE=InnoDB;

CREATE TABLE Favorite(
	id INTEGER UNSIGNED AUTO_INCREMENT,
	substituted_id INTEGER UNSIGNED NOT NULL,
	substitute_id INTEGER UNSIGNED NOT NULL,
	PRIMARY KEY(id),
    CONSTRAINT fk_substituted_id
		FOREIGN KEY (substituted_id)
		REFERENCES Product(id),
	CONSTRAINT fk_substitute_id
		FOREIGN KEY (substitute_id)
		REFERENCES Product(id)
	)ENGINE=InnoDB;

CREATE TABLE nutriscore(
	id INTEGER UNSIGNED AUTO_INCREMENT,
	score VARCHAR(1) NOT NULL,
	PRIMARY KEY(id)
    )ENGINE=InnoDB;

ALTER TABLE Category_product ADD CONSTRAINT fk_category_id FOREIGN KEY (id) REFERENCES category(id);
ALTER TABLE Category_product ADD CONSTRAINT fk_product_id FOREIGN KEY (id) REFERENCES product(id);
ALTER TABLE product ADD CONSTRAINT fk_nutriscore_id FOREIGN KEY (id) REFERENCES nutriscore(id);
INSERT INTO nutriscore(score)
VALUES ('A'), ('B'), ('C'), ('D'), ('E');
