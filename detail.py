import urllib.request as fetch
import re
import random
from time import sleep
import psycopg2 as pg

conn=pg.connect(database='Pokemon',password='B1992!R@Lz',user='postgres',port=5433)

cur=conn.cursor()

