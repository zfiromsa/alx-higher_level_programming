#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

create_table_query="CREAT TABLE IF NOT EXISTS $D=database.second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);"

mysql -u root -p -e "create_table_query"

insert_que="
    INSERT INTO $database.second_table (id, name, score) VALUE(1, 'John', 10)
    INSERT INTO $database.second_table (id, name, score) VALUE(2, 'Alex', 3)
    INSERT INTO $database.second_table (id, name, score) VALUE(3, 'Bob', 14)    
    INSERT INTO $database.second_table (id, name, score) VALUE(4, 'George', 8)
"

mysql -u root -p -e "$insert_que"

