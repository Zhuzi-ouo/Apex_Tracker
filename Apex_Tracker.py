import requests
from bs4 import BeautifulSoup
def AT(User):
    response=requests.get(f"https://tracker.gg/apex/profile/origin/{User}/overview")
    soup=BeautifulSoup(response.text,"html.parser")
    Apextracker=soup.find_all("span",class_="value")
    Apexrank=soup.find_all("span",class_="mmr")
    AT.Level=Apextracker[0].string
    AT.BRR=Apexrank[0].text
    AT.AR=Apexrank[1].text
