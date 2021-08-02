import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    ExtractData=data.json()
    completedlist=[i for i in ExtractData if i['completed']==True]
    for i in completedlist:
        print(i)

except:
    print("Please check the link if it is not correct")