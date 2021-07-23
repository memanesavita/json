import json
from os import close
w=open("sa.json","r")
data=json.load(w)
# print(data)
print(data)
w.close()
