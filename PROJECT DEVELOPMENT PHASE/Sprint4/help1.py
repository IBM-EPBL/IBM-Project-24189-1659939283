import requests
from bs4 import BeautifulSoup # Webscrape
from collections import defaultdict # Default dictionary: store a list with each key
import pandas as pd 
import csv
import os
import json

url = "https://indeed11.p.rapidapi.com/"
p=1
payload = {
	"search_terms": "Marketing",
	"location": "United States",
	"page": "1"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "9381357d88msha354337c2eb1e98p1348a7jsn192d84997537",
	"X-RapidAPI-Host": "indeed11.p.rapidapi.com"
}
main_dir = os.getcwd() + '\\'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print('Base Directory Created Successfully.')
# Name of the CSV File
file_name = 'Jobs1.csv'
# Path of the CSV File
file_path = main_dir + file_name
response = requests.request("POST", url, json=payload, headers=headers)
html=response.text
dict=json.loads(html)
print(dict)
