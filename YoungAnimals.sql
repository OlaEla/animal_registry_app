-- Удаляем таблицу, если она уже существует
DROP TABLE IF EXISTS YoungAnimals;

-- Создаем таблицу YoungAnimals с расчетом возраста
CREATE TABLE YoungAnimals AS
SELECT 
    id,
    name,
    birthDate,
    genius_id,
    TIMESTAMPDIFF(MONTH, birthDate, CURDATE()) AS age_in_months
FROM 
    KennelAnimal
WHERE 
    TIMESTAMPDIFF(YEAR, birthDate, CURDATE()) >= 1
    AND TIMESTAMPDIFF(YEAR, birthDate, CURDATE()) < 3;
