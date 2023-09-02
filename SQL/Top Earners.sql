-- https://www.hackerrank.com/challenges/earnings-of-employees

-- We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.

SELECT earnings, count(*) as counting
FROM (SELECT *, months*salary as earnings FROM Employee) AS new
GROUP BY earnings
HAVING earnings=max(earnings)
ORDER BY counting desc
LIMIT 1;

-- Other way:

-- SELECT 
--     (salary*months) AS ttl_sal, 
--     COUNT(salary*months) 
-- FROM employee 
-- WHERE 
--     (salary*months)=(SELECT MAX(salary*months) FROM employee) GROUP BY (salary*months);
