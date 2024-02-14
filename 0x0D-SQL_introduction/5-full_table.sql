--- A script that prints the full description of the table first_table from 
--- the database hbtn_0c_0 in your MySQL serve

SELECT COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = '$database' AND TABLE_NAME = 'first_table';
