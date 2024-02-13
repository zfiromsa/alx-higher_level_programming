#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

update_que="UPDATE {$database}.second_table SET score = 10 WHERE name = 'Bob';"
mysql -u root -p -e "$update_que" $database

