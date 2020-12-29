from bs4 import BeautifulSoup
import requests
import datetime
import json, sys, os

try:
    sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
finally:
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

    with open(os.path.join(BASE_DIR, "json", "todaysprice.json"), 'w') as f:
        json.dump(container, f)


def liveprice():
    URL = "http://www.nepalstock.com/stocklive"
    categories = ('S.N.', 'Symbol', 'LTP', 'LTV', 'PointChange', 'PercChange', 'Open', 'High', 'Low', 'Volume', 'PrevClosing')


    response = requests.get(URL).text
    soup = BeautifulSoup(response, features="html.parser")
    td = soup.find_all("td")
    
    container, count = scrape(td[11:], categories, 1)
    print(container)

def floorsheet():
    URL = "http://www.nepalstock.com/main/floorsheet/"

    titles = ("Contract No.", "Symbol", "Buyer Broker", "Seller Broker"
             ,"Quantity", "Rate", "Amount")
    floorsheet = []

    while True:
        print(f"Visiting {URL}...")
        response = requests.get(URL).text 
        soup = BeautifulSoup(response, "html.parser")
        rows = soup.find_all("tr")[2:-2]

        for row in rows:
            tds = row.find_all("td")[1:]
            page = {}
            for k, v in zip(titles, tds):
                page[k] = v.text.strip()
            
            if page:
                floorsheet.append(page)

        next_p = soup.find("a", attrs={"title": "Next Page"})
        print(f"Next URL...{next_p}")
        if not next_p:
            break
        URL = next_p["href"]
    
    with open(os.path.join(BASE_DIR, "json", "floorsheet.json"), 'w') as f:
        json.dump(floorsheet, f)


def listcompany():
    index = 1
    companies = []
    titles = "Name", "Symbol", "Sector"

    while index < 15:
        URL = f"http://www.nepalstock.com/company/index/{index}"
        response = requests.get(URL).text
        soup = BeautifulSoup(response, 'html.parser')
        rows = soup.find_all("tr")
        t_rows = rows[2:]

        for r in t_rows:
            tds = r.find_all("td")[2:5]
            company = {}
            for k, v in zip(titles, tds):
                company[k] = v.text.strip()
            
            if company:
                companies.append(company)

        index += 1
    
    with open(os.path.join(BASE_DIR, "json", "companylist.json"), 'w') as f:
        json.dump(companies, f)


if __name__ == "__main__":
    # listcompany()
    floorsheet()