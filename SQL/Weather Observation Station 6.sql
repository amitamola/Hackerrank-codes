-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiou]';

-- Other ways:
-- SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u');

-- select distinct(city) from station where city like 'A%' OR city like 'E%' OR city like 'I%' OR city like 'O%' OR city like 'U%' order by city ASC;
