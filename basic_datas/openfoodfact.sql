SET NAMES utf8;
SET CHARACTER
SET "utf8";
DROP DATABASE IF EXISTS openfoodfact;
CREATE DATABASE openfoodfact;
USE openfoodfact;

CREATE TABLE category(
	id INTEGER UNSIGNED AUTO_INCREMENT UNIQUE ,
	name VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
	)ENGINE=InnoDB;

CREATE TABLE category_product(
	id INTEGER UNSIGNED AUTO_INCREMENT,
    category_id INTEGER UNSIGNED NOT NULL,
    product_id INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(id)
    )ENGINE=InnoDB;

CREATE TABLE product(
	id INTEGER UNSIGNED AUTO_INCREMENT UNIQUE,
	name VARCHAR(400) NOT NULL,
	code VARCHAR(100) NOT NULL,
    description VARCHAR(800) ,
    url VARCHAR(400) NOT NULL,
    store VARCHAR(400),
	nutriscore_id INTEGER UNSIGNED,
	PRIMARY KEY(id)
	)ENGINE=InnoDB;

ALTER TABLE product MODIFY COLUMN store VARCHAR(400)
CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE category MODIFY COLUMN name VARCHAR(200)
CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE Favorite(
	id INTEGER UNSIGNED AUTO_INCREMENT UNIQUE,
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

ALTER TABLE  category ADD CONSTRAINT unique_name UNIQUE (name);
CREATE UNIQUE INDEX uk_categories ON category(id, name);

ALTER TABLE  product ADD CONSTRAINT unique_code UNIQUE (code);
CREATE UNIQUE INDEX uk_products ON product(id, code);
CREATE UNIQUE INDEX uk_favorite ON favorite(substituted_id, substitute_id);
ALTER TABLE category_product ADD CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES category(id);
ALTER TABLE category_product ADD CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product(id);
ALTER TABLE product ADD CONSTRAINT fk_nutriscore_id FOREIGN KEY (nutriscore_id) REFERENCES nutriscore(id);
INSERT INTO nutriscore(score)
VALUES ('a'), ('b'), ('c'), ('d'), ('e');

