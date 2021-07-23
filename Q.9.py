# Question 8

# Q8.Tumhare pass four employes ki details hai list mai:-
# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. 
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. 
# Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai. 
import json
# from os import name
x={"shoppin list":{
"chaco":"15",
"biscut":"12",
"cadboury":"10",
"vadapav":"20"}

}

print(type(x))
with open("shopping.json","w")as f:
    json.dump(x,f,indent=4)
name=input("which you want to buy")
itms=int(input("how many item you want"))
for keys in x:
    for value in x:
        for i,k in x[keys].items():
            if i==name:
                t=int(k)-itms
                print(t)


