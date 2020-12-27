import json, datetime, os, sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nepsense.settings import BASE_DIR
from psycopg2 import connect, Error

def main():
    global LATEST_DATE
    try:
        conn = connect(
            dbname = "nepsense",
            user = "isharm",
            password = "ishar123",
            host = "localhost",
            connect_timeout = 3
        )

        cur = conn.cursor()
    except (Exception, Error) as err:
        print ("\npsycopg2 connect error:", err)
        conn = None
        cur = None

    with open(os.path.join(BASE_DIR, 'json/todaysprice.json'), 'r') as f:
        share_price = json.load(f)

    table = 'market_stock'
    cols = 'sn', 'company', 'transno', 'maxp', 'minp', 'closep', 'tradedshares', 'amount', 'prevclosep', 'diff', 
    sql_string = f"INSERT INTO {table} " + "(" + ','.join(cols) + ")" " VALUES ("
    query = sql_string

    # cur.execute(f"DELETE FROM {table}")
    # conn.commit()

    for row in share_price:
        for k, v in row.items():
            try:
                if isinstance(v, str) and float(v):
                    pass
            except:
                v = f"\'{v}\'"
            query += str(v) + ','

        query = query[:-1] + ')'
        cur.execute(query)
        conn.commit()
        query = sql_string
    
    LATEST_DATE = datetime.date.today()
    with open(os.path.join(BASE_DIR, 'updated_date'), 'w') as f:
        f.write(str(LATEST_DATE))
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()