from bs4 import BeautifulSoup
import requests
import datetime
import json, sys, os

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nepsense.settings import BASE_DIR

def scrape(souplist, categories, count, max=None):
    container = []
    counter = 0
    row = {}
    for t in souplist:
        if max and max == count:
            break
        if not counter:
            row[categories[counter]] = count
        else:
            row[categories[counter]] = t.text.strip()
        counter += 1
        if not counter < len(categories):
            container.append(row)
            counter = 0
            count += 1
            row = {}
    
    return container, count

def todaysprice():
    index = 1
    categories = ('S.N.', 'Traded Company', 'No. of trans', 'MaxPrice', 'MinPrice',
                    'ClosePrice', 'TradeShares', 'Amount', 'PrevClose', 'Diff')

    container = []

    count = 1
    while index <= 10:
        URL = f"http://www.nepalstock.com/main/todays_price/index/{index}/"
        response = requests.get(URL).text
        print(f"{URL}...")
        soup = BeautifulSoup(response, features="html.parser")
        td = soup.find_all("td")[11:]

        con, count = scrape(td, categories, count)
        container.extend(con)
        index += 1
    
    return container


def liveprice():
    URL = "http://www.nepalstock.com/stocklive"
    categories = ('S.N.', 'Symbol', 'LTP', 'LTV', 'PointChange', 'PercChange', 'Open', 'High', 'Low', 'Volume', 'PrevClosing')


    response = requests.get(URL).text
    soup = BeautifulSoup(response, features="html.parser")
    td = soup.find_all("td")
    
    container, count = scrape(td[11:], categories, 1)
    print(container)

def floorsheet():
    pass



def main():
    stock = todaysprice()

    with open(os.path.join(BASE_DIR, "json", "todaysprice.json", 'w')) as f:
        json.dump(stock, f)



if __name__ == "__main__":
    update = datetime.time(hour=15)
    while True:
        today = datetime.datetime.now()
        if today.weekday() in range(0, 5):
            main()
            break