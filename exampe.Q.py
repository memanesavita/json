
import json
a={"k":90,"y":56,"h":89}
max=open("sa.json","w")
json.dump(a,max,indent=4)
print(max)