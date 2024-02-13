#!/usr/bin/bash
-- A script that lists all the tables of a database in your MySQL server.

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"
mysql -u root -p -e "USER $database; SHOW TABLE;"
