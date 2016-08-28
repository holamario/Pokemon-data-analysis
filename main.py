import urllib.request as fetch
import re
import random
from time import sleep
import psycopg2 as pg

conn=pg.connect(database='Pokemon',password='B1992!R@Lz',user='postgres',port=5433)

cur=conn.cursor()
cur.execute("""create table if not exists pokemon.basic_info(id serial PRIMARY KEY ,index INTEGER ,name CHAR ,is_final INTEGER )""")
conn.commit()
url='http://pokemondb.net/pokedex/national'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

resp=fetch.Request(url=url,headers=headers)
response=fetch.urlopen(resp).read().decode('utf8')
print(response)

pattern=re.compile('<span class="infocard-tall "><a class="pkg " data-sprite=".*?" href="/pokedex/.*?"></a><br><small>#(.*?)</small><br><a class="ent-name" href="/pokedex/.*?">(.*?)</a><br><small class="aside">.*?</small></span>',re.S)
result=re.findall(pattern,response)

if result:
    for each in result:
        print(each)
        cur.execute("""insert into pokemon.basic_info(index,name,is_final) values(%s,%s,%s)""",(each[0],each[1],0))
    conn.commit()
else:
    print('wrong')