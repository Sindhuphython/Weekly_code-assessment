import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    E=data.json()
    List=[]
    List_Of_True=[i for i in E if i["completed"]==True]
    List.append(List_Of_True)
    print(List)

except:
    print("Please check the link if it is not correct")

else:
    print("We got details for True information")

finally:
    print("Good job, task completed ")