-- SQL-скрипт для создания таблиц
CREATE TABLE Commands
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор команды',
    name varchar(30) NOT NULL COMMENT 'Название команды',
    description varchar(255) COMMENT 'Описание команды',
    INDEX (name)
);

CREATE TABLE AnimalGroup
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор группы',
    name varchar(30) NOT NULL COMMENT 'Название группы животных',
    INDEX (name)
);

CREATE TABLE AnimalGenius
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор вида',
    name varchar(30) NOT NULL COMMENT 'Название вида',
    group_id INT NOT NULL COMMENT 'ID группы, к которой относится вид',
    FOREIGN KEY (group_id) REFERENCES AnimalGroup (id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX (name)
);

CREATE TABLE KennelAnimal
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор животного',
    name varchar(30) NOT NULL COMMENT 'Имя животного',
    birthDate DATE NOT NULL COMMENT 'Дата рождения животного',
    genius_id INT NOT NULL COMMENT 'ID вида животного',
    FOREIGN KEY (genius_id) REFERENCES AnimalGenius (id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX (name)
);

CREATE TABLE AnimalCommands
(
    animal_id INT NOT NULL COMMENT 'ID животного',
    command_id INT NOT NULL COMMENT 'ID команды',
    PRIMARY KEY (animal_id, command_id),
    FOREIGN KEY (animal_id) REFERENCES KennelAnimal (id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (command_id) REFERENCES Commands (id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
