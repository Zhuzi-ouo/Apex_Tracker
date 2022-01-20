User=input ("Enter Your Apex Username:")
import requests
from bs4 import BeautifulSoup

response=requests.get(f"https://tracker.gg/apex/profile/origin/{User}/overview")
soup=BeautifulSoup(response.text,"html.parser")
Apextracker=soup.find_all("span",class_="value")
Apexrank=soup.find_all("span",class_="mmr")
print ("Level",Apextracker[0].string)
print ("Battle Royale Rank",Apexrank[0].text)
print ("Arenas Rank",Apexrank[1].text)
