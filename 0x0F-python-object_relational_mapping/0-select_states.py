#!/usr/bin/python3
"it lists all states from the database hbtn_0e_0_usa:"


if __name__ == "__main__":
    import MySQLdb
    import sys

    try:
        db = MySQLdb.connect(host="localhost", port=3306,user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.arg[3])
        
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print("ERROR: ", err)

    finally:
        if db:
            cur.close()
            db.close()

