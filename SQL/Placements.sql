-- https://www.hackerrank.com/challenges/placements/problem

-- You are given three tables: Students, Friends and Packages. Students contains two columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

-- Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.

CREATE VIEW own_sal AS
SELECT ID, NAME, SALARY
FROM Students
INNER JOIN Packages
USING(ID);

CREATE VIEW fren_sal AS
SELECT Friends.ID, Friend_ID, SALARY as Friend_Salary
FROM Friends
INNER JOIN Packages
ON Friends.Friend_ID=Packages.ID;

CREATE VIEW final AS
SELECT own_sal.ID, NAME, SALARY, Friend_ID, Friend_Salary
FROM own_sal
INNER JOIN fren_sal
ON own_sal.ID=fren_sal.ID
ORDER BY fren_sal.Friend_Salary;

SELECT NAME
FROM final
WHERE Friend_Salary>Salary;

-- OTHER WAYS:

-- SELECT Name FROM Students
-- JOIN Friends USING (ID)
-- JOIN Packages AS student_salary USING (ID) 
-- JOIN Packages AS friend_salary ON friend_salary.ID = Friends.Friend_ID
-- WHERE friend_salary.Salary > student_salary.Salary
-- ORDER BY friend_salary.salary;
