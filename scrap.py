import requests
import json
from bs4 import BeautifulSoup

header = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}


address=[]
top = []
dict = {}
tops=[]

def topAccounts():

    apitoken="FMPY7CZC816282C49VUN44R8MHYIAQQG9V"

    for i in range(1,5):
        r = requests.get("https://etherscan.io/accounts/{i}", headers=header)
        soup = BeautifulSoup(r.content, "lxml")
        for el in soup.find("tbody").find_all("a"):
            address.append(el.get_text())

    for i in range(0,len(address)-10):
        link = "https://api.etherscan.io/api?module=account&action=balance&address=" + address[i] + "&tag=latest&apikey="+apitoken
        r = requests.get(link, headers=header)
        soup = BeautifulSoup(r.content, "lxml")

        dict[i] = json.loads(soup.find("body").get_text())

    

    for i in range(0,len(address)-10):
        tops.append({
            "category":address[i],
            "num_of_products":dict[i]['result']
        })

    return tops