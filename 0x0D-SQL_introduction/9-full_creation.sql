-- A script that creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server and add multiples rows.
CREAT TABLE IF NOT EXISTS $D=database.second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);

INSERT INTO $database.second_table (id, name, score) VALUE(1, 'John', 10);
INSERT INTO $database.second_table (id, name, score) VALUE(2, 'Alex', 3);
INSERT INTO $database.second_table (id, name, score) VALUE(3, 'Bob', 14);
INSERT INTO $database.second_table (id, name, score) VALUE(4, 'George', 8);
