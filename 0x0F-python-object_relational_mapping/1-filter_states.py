#!/usr/bin/python3
"that lists all states with a name starting with N(upper N) from the database"


if __name__ == "__main__":
    import MySQLdb
    import sys

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)
    except MySQLdb.Error as err:
        print("ERROR: ", err)

    finally:
        if db:
            cur.close()
            db.close()

