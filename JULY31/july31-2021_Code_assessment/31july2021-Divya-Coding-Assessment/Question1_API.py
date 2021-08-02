import json
import  requests
data = requests.get ("https://jsonplaceholder.typicode.com/todos")
Extractdata = data.json()
completed_List = [ ]


Data_list_details = [i for i in Extractdata if i["completed"]==True]
completed_List.append(Data_list_details)
print(completed_List)

