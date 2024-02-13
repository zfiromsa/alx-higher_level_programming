#!/usr/bin/bash
--a script that inserts a new row in the table first_table
--(database hbtn_0c_0) in your MySQL server.

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

sql_que="INSERT INTO $database.first_table (id, name) VALUES (89, 'Best School');"
mysql -u root -p -e "sql_que"
