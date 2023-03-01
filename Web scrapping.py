import requests
from bs4 import BeautifulSoup
import pandas
import sqlite3
def connect_db(dbname):
    conobj = sqlite3.connect(dbname)
    conobj.execute("create table if not exists ElonMusk (Name text, DOB text, Education text, CEO text, Founder text, Co_Founder text)")    
    print("Table succcessfull created")
    conobj.close()
def insert_db(dbname,vals):
    conobj=sqlite3.connect(dbname)
    insert_cmd=("insert into ElonMusk(Name,DOB,Education,CEO,Founder,Co_Founder) values (?,?,?,?,?,?)")
    conobj.execute(insert_cmd,vals)
    conobj.commit()
    conobj.close()
def get_hotel_info(dbname):
    conobj=sqlite3.connect(dbname)
    curobj=conobj.cursor()
    curobj.execute("select * from ElonMusk")
    data=curobj.fetchall()
    for i in data:
        print(i)
    conobj.close()
web_url="https://en.wikipedia.org/wiki/Elon_Musk"
scrape_list=[]
connect_db("elon_musk.db")


req = requests.get(web_url)
content=req.content
soup = BeautifulSoup(content,"html.parser")
em_data = soup.find_all("table",{"class":  "infobox biography vcard"})
    
for em in em_data:
    em_dict={}
    em_dict["Name"]=em.find("div",{"class":"fn"}).text
    em_dict["DOB"]=em.find("span",{"class":"bday"}).text
    em_dict["Education"]=em.find("a",{"title": "University of Pennsylvania"}).text+", "+ em.find("a",{"title":"Bachelor of Arts"}).text+", "+ em.find("a",{"title":"Bachelor of Science"}).text
    em_dict["CEO"]=em.find("a",{"title":"Tesla, Inc."}).text +", "+ em.find("a",{"title":"SpaceX"}).text+", "+ em.find("a",{"title":"Twitter, Inc."}).text
    em_dict["Founder"]=em.find("a",{"title":"SpaceX"}).text+", "+ em.find("a",{"title":"The Boring Company"}).text+", "+ em.find("a",{"title":"X.com"}).text
    em_dict["Co_Founder"]=em.find("a",{"title":"Neuralink"}).text+", "+ em.find("a",{"title":"OpenAI"}).text+", "+ em.find("a",{"title":"Zip2"}).text
    scrape_list.append(em_dict)
    print(scrape_list)

insert_db("elon_musk.db", tuple(em_dict.values()))

data_frame = pandas.DataFrame(scrape_list)
data_frame.to_csv("elon_musk.csv") 
get_hotel_info("elon_musk.db")
