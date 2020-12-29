import json, datetime, os, sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nepsense.settings import BASE_DIR
from psycopg2 import connect, Error


def load_todaysprice(cur, conn):
    with open(os.path.join(BASE_DIR, 'json/todaysprice.json'), 'r') as f:
        share_price = json.load(f)

    table = 'market_stock'
    cols = 'sn', 'company', 'transno', 'maxp', 'minp', 'closep', 'tradedshares', 'amount', 'prevclosep', 'diff', 'symbol'
    sql_string = f"INSERT INTO {table} " + "(" + ','.join(cols) + ")" " VALUES ("
    query = sql_string

    # cur.execute(f"DELETE FROM {table}")
    # conn.commit()

    for row in share_price:
        for i, (k, v) in enumerate(row.items()):
            try:
                if isinstance(v, str) and float(v):
                    pass
            except:
                v = f"\'{v}\'"
            query += str(v) + ','

            if i == 1:
                comp = v

        cur.execute(f"SELECT symbol FROM company_list WHERE name={comp}")
        symbol = cur.fetchone()
        if symbol:
            query += f"'{symbol[0]}'" + ")"
            prev = symbol[0]
        else:
            query += f"'{prev}'" + ")"

        cur.execute(query)
        conn.commit()
        query = sql_string

def load_floorsheet(cur, conn):
    with open(os.path.join(BASE_DIR, 'json/floorsheet.json'), 'r') as f:
        floorsheet = json.load(f)

    table = "market_floorsheet"
    cols = "contractnum", "symbol", "buyerbroker", "sellerbroker", "quantity", "rate", "amount" 
    sql_string = f"INSERT INTO {table} " + "(" + ','.join(cols) + ")" " VALUES ("
    query = sql_string

    for row in floorsheet:
        for k, v in row.items():
            try:
                if isinstance(float(v), float) or isinstance(int(v), int):
                    query += v + ','            
                    continue
            except:
                query += f"'{v}'" + ','

        query = query[:-1] + ')'
        cur.execute(query)
        conn.commit()
        query = sql_string
        

def load_companylist(cur, conn):
    with open(os.path.join(BASE_DIR, 'json/companylist.json'), 'r') as f:
        comp_list = json.load(f)
    
    table = "company_list"
    cols = "name", "symbol", "sector"
    sql_string = f"INSERT INTO {table} " + "(" + ','.join(cols) + ")" " VALUES ("
    query = sql_string

    # cur.execute(f"DELETE FROM {table}")
    # conn.commit()

    for company in comp_list:
        for v in company.values():
            query += f"'{v}'" + ','
        
        query = query[:-1] + ')'
        print(f"Executing |- {query} -|")
        cur.execute(query)
        conn.commit()
        query = sql_string
        


def main():
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

    load_floorsheet(cur, conn)
    
    LATEST_DATE = datetime.date.today()
    with open(os.path.join(BASE_DIR, 'updated_date'), 'w') as f:
        f.write(str(LATEST_DATE))
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()