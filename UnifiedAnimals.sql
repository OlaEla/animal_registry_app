-- Удаляем таблицу, если она уже существует
DROP TABLE IF EXISTS UnifiedAnimals;

-- Создаем объединенную таблицу
CREATE TABLE UnifiedAnimals AS
SELECT 
    id,
    name,
    birthDate,
    genius_id,
    'KennelAnimal' AS source_table
FROM 
    KennelAnimal

UNION ALL

SELECT 
    id,
    name,
    birthDate,
    genius_id,
    'HorseAndDonkey' AS source_table
FROM 
    HorseAndDonkey

UNION ALL

SELECT 
    id,
    name,
    birthDate,
    genius_id,
    'YoungAnimals' AS source_table
FROM 
    YoungAnimals;
