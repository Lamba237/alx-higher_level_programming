-- a script that computes the score average of all records in the table
-- second_table of the database hbtn_0c_0 in your MySQL server.

ALTER TABLE  `second_table`
ADD `average` FLOAT(8);

SELECT AVG(`score`) AS `average`
FROM second_table;
