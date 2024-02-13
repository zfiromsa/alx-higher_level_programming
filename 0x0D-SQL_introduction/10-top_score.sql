#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

sql_que="SELECT score, name FROM {$database}.second_table ORDER BY score DESC"
mysql -u root -p -e "$sql_que" $database
