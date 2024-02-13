#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

delete_que="DELETE FROM {$database}.second_table WHERE score <= 5;"
mysql -u root -p -e "$delete_que" $database

