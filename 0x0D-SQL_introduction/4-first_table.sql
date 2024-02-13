#!/usr/bin/bash
-- A script that creates a table called first_table in
-- the current database in your MySQL server.

if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"
sql_scr=$(cat <<EOF
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
EOF
)

echo "$sql_scr" | mysql -u root -p "$database"
