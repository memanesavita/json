# Question 2

# Q.2 Python object ko json data main convert karne ka program likho? 

import json

sun={"name": "David",
     "class":"I",
     "age": 6  
 }
k=open("aa.json","w")
json. dump(sun,k,indent=4)
print(k)



