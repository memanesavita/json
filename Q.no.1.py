# Question 1

# Q.1 Json data ko python object main convert karne ka program likho?. 

import json
marsh={"Name":"Ram",
     "Class":"IV", 
     "Age":9 }

tree=open("k.json","w")
json.dump(marsh,tree,indent=4)
print(tree)