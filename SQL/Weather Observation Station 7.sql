-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[aeiou]$';

-- Other solutions:
-- SELECT DISTINCT CITY FROM STATION WHERE LOWER(RIGHT(CITY,1)) IN ('a','e','i','o','u');

-- select distinct(city) from station where city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';
