#n = [1,3,6,6,7,10,10,1]
#m = []
#for item in n:
   #if item not in m:
   # m.append(item)
#print(m)



""" list1 = [1,2,3,5]
tuple = (0,2,4,6,7)
a,b,c,d = list1
x,y,z,s,h = tuple
print(a,b,c,d)
print(x,y,z,s,h)"""

"""names = [[1,2,3],[4,5,6,7]]
print(names)
names1 = ((8,9,10),(11,12,13,14))
print(names1)
a,b = names
print(a[0],b[1])"""

"""name = {'a','b'}
for items in name:
    print(items)"""


"""name = {'a','b'}
for items in name:
    print(items)"""

"""name = {'a','b','a'}
for items in name:
    print(items)"""


"""x = [1,2,3,4,5,4,1]
y = set(x)
print(y)
z = list(y)
print(z)
print(z[1])"""

"""dict = {"name":"ram","email":"ram123","sal":"50k"}
print(dict)
print(dict["email"])
print(dict["sal"])
for items in dict:
    print(dict[items])"""

"""emp = {"name":"ram","email":"ram123","sal":"50k","marks":[100,98,90,80],"address":{"pincode":1234,'stree':987,'location':'near bus top',"surname":{"sn":"neluri"}},"ph":{"phone":123456,"city":{"city name":"atp"}},"hobbies":{"hobbi":"playing chess"}}
name1 = emp["name"]
print(name1)
email = emp["email"]
print(email)
mark = emp["marks"]
print(mark)
mark1 = mark[0]
print(mark1)
addres = emp["address"]['location']
print(addres)
pin = emp["address"]["pincode"]
print(pin)
sur = emp["address"]["surname"]["sn"]
print(sur)
p = emp["ph"]["phone"]
print(p)
cit = emp["ph"]["city"]["city name"]
print(cit)
hob = emp["hobbies"]["hobbi"]
print(hob)"""

emp = {"name":"ram","email":"ram123","sal":"50k","marks":[100,98,90,80],"address":{"pincode":1234,'stree':987,'location':'near bus top',"surname":{"sn":"neluri"}},"ph":{"phone":123456,"city":{"city name":"atp"}},"hobbies":{"hobbi":"playing chess"}}
for items in emp:
   print(type(emp[items]),emp[items])
print(emp["sal"])
print(emp["address"]["stree"])
print(emp["hobbies"]["hobbi"])

print(emp["marks"])


    



