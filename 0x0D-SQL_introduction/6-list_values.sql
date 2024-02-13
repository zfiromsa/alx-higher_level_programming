#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

sql_que="SELECT * FROM $database.first_table;"

mysql -u root -p -e "sql_que"
