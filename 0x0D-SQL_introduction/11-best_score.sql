#!/usr/bin/bash

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

select_que="SELECT score, name FROM {$database}.second_table WHERE score >= 10 BY score DESC"
mysql -u root -p -e "$select_que" $database

