#!/usr/bin/bash
---


if [ $# -ne 1]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"

sql_que=$(cat <<EOF
SELECT COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = '$database' AND TABLE_NAME = 'first_table';
EOF
)

mysql -u root -p -e "$sql_que"
