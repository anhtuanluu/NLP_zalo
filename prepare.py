import json
from bs4 import BeautifulSoup
import torch
import csv
#label=set()
label=['substitution', 'goal_info', 'match_info', 'match_result', 'penalty', 'card_info']
#label=['substitution', 'goal_info', 'card_info']
count=0
file_csv=open('train_zalo2.csv', mode='w')
employee_writer = csv.writer(file_csv, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
with open('data/train/train.jsonl','rb') as json_file:
    json_list = list(json_file)
for json_str in json_list:
    doc = json.loads(json_str)
    for html in doc["html_annotation"]:
        soup = BeautifulSoup(html)
        events = soup.find_all("span", {"class": "tag"})
        event2 = soup.find_all("span")
        for e in events:
            print(e)
            #print("event_type:", e["data"])
            event_types=e["data"]
            for event_type in e["data"].split(":")[1:-1]:
                count=count+1
                print(event_type)
                #label.add(event_type)
                for i in range(0,len(label)):
                    if label[i]==event_type:
                        #employee_writer.writerow(['train_'+str(count), e.text, i])
                        print(i)
            print("event_id:", e["event_id"])
            # print("text:", e.text)


            # print(label)
