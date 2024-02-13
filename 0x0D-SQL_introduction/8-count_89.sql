#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

sql_que="SELECT COUNT(*) FROM $database.first_table WHERE i = 89;"
mysql -u root -p -e "sql_que" | tail -n 1

