-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

-- NOTE - Key here is not to forget space when using Regex

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiou][A-z ]+[aeiou]$';

-- select distinct(city) from station where city REGEXP'[AEIOU]$' AND city REGEXP'^[AEIOU]';

