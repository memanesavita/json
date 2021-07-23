
# Question 8

# Q8.Tumhare pass four employes ki details hai list mai:-
# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye. 
# aur ye sab dictionary ki keys hai jismai maine list main value di hai.
# Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai

# Tumhare pass four employes ki details hai list mai:

import json


a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]  

emp1={}
emp2={}
emp3={}
emp4={}

x={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp3}
for i in range(len(a)):
    emp1.update({d[i]:a[i]})
for j in range (len(b)):
    emp2.update({d[j]:b[j]})
for k in range(len(c)):
    emp3.update({d[k]:c[k]})
for a in range(len(d)):
    emp4.update({d[a]:d[a]})
with open("savita.json","w") as t:
    json.dump(x,t,indent=4)







