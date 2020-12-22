import json, datetime
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

    with open('/home/isharm/go/github.com/IsharMhzn/nepse-scrapi/json/todaysprice.json', 'r') as f:
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
    with open('updated_date', 'w') as f:
        f.write(str(LATEST_DATE))
    cur.close()
    conn.close()

if __name__ == "__main__":
    update = datetime.time(hour=15)
    while True:
        today = datetime.datetime.now()
        if today.weekday() in range(0, 5):
            if today.time() > update:
                main()
                print("Database updated")
            else:
                print("Not time yet")
        else:
            print("Stock market closed today")