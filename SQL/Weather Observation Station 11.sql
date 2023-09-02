-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
-- https://www.hackerrank.com/challenges/weather-observation-station-11

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiou][A-z ]+' OR CITY REGEXP '[A-z ]+[^aeiou]$';
