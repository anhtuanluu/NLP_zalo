import json
from bs4 import BeautifulSoup
import torch
import csv
count=0
file_csv=open('public_test_zalo.csv', mode='w')
employee_writer = csv.writer(file_csv, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
with open('data/public_test/public_test/public_test.jsonl','rb') as json_file:
    json_list = list(json_file)
for json_str in json_list:
    doc = json.loads(json_str)
    #print(doc)
    #print(doc["original_doc"]["_source"]["body"][0]["text"])
    for i in range(0,len(doc["original_doc"]["_source"]["body"])):
        count=count+1
        employee_writer.writerow(['public_test_'+str(count),doc["original_doc"]["_source"]["body"][i]["text"]])