import json
file ="data.text"
dict={}
with open (file) as saral:
    for line in saral:
        command,discription=line.strip().strip(None,1)
        dict[command]=discription.strip()
out_file=open("text.json","W")
json.dump(dict,out_file,indent=4)
out_file.close()














