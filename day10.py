"""emp = {"name":"abcd","id":1}
empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
for item in empList:
    print('name',item['name'],'id',item['id'])

    def display_emp_list():
    emp = {"name":"abcd","id":1}
    empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
    for item in empList:
        print('name',item['name'],'id',item['id'])
display_emp_list()



def display_emp_list(marks):
   print(marks)
display_emp_list([1,2,3,4])"""


"""emp = {"name":"ram","id":1,"email":"ram123"}
emp2 = [{"name":"laxman","id":2,"email":"laxman122"}, {"name":"bharath","id":3,"email":"bharath122"}]
print(emp2[0])
print(emp2[1])
print(emp)
for item in emp2:
    print(emp2)
    print(item)
    print('name',item['name'],'id',item['id'])"""

"""def display_emp_list(marks,x):
    print(marks)
    for items in marks:
        res = items*x
        if res % 2 == 0:
            print("even number",res)
        else:
            print("odd number",res)    
display_emp_list([1,2,3,4,5,6,7,8,9,10],3)"""


"""n = [1,2,3,4,5,6]
n[0]=100
print(n)
print(len(n))"""


"""def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
print_numbers(10)"""


"""number = [1,2,3,4]
print(number)
for item in number:
    print(item)


number1 = ("ram","laxman","seetha","ram")
print(number1)
for items in number1:
    print(items)

names = {"oormila","bharath","kousalya"}
print(names)
for items in names:
    print(items)

names1 = {"name":"ram","email":"ram123","ph":123456}
for items1 in names1:
    print(items1) 

x = 10
y = 20
z = x + y
print(z)

def printing_numbers(number):
 print(number)
 for items2 in number:
    print(items2)
printing_numbers([1,2,3])

marks = [1,2,3,4,5,6,7,8,9]
for items3 in marks:
    if items3 % 2 != 0:
        print("odd",items3)
    else:
        print("even",items3) 


list3 = [1,2,3,4,1,5,3,2]
list2 = set(list3)
print(list2)
list3 = list(list2)
print(list3)

tuple1 = ("arjun","bhema","nakul","arjun")
print(tuple1)
tuple2 = list(tuple1)
print(tuple2)
tuple2.append("sahadev")
print(tuple2)
tuple3 = set(tuple1)
print(tuple3)
tuple4 = list(tuple3)
print(tuple4)
print(tuple4[0])

dict1 = {"name":"sarada","addres":"atp","marks":[20,30,70],"name":"sarad"}
print(dict1)
for i in dict1:
   print(dict1[i])
   print(dict1["name"])
dict2 = set(dict1)
print(dict2)

def display_names(name):
    for i2 in name:
        print(i2)
display_names({"name":"ram","email":"seetha123"})
display_names([1,2,3,4])
display_names(("bharath","laxman"))
display_names({"sunil","supri","sunil"})"""

"""def display_names(a):
    for i in a:
        print(i)
    x,y,z = a 
    print(a)
    print(x)
    print(y)
    print(z)
    s = x+y
    j = x/z
    h = y*z
    print(s)
    print(j)
    print(h)
display_names((1,2,3)) 
display_names([30,50,90])
display_names({"ram","seetha","bharath"}) 
display_names({"name":"arjun","email":"arjun123","ph":12345}) """  


"""def display_value(p,t,r):
 z = p*t*r/100
 print(z)
display_value(20000,12,2)
display_value(35000,8,2)
display_value(85000,24,2)
display_value(100000,6,2)"""

"""def display_value(a,b,c):
    if c == '+':
        print(a+b)
    elif c =='-':
        print(a-b)
    elif c =='*':
        print(a*b)
    elif c =='/':
        print(a/b)
    elif c == '%':   
        print(a%b)
display_value(10,5,'+') 
display_value(10,5,'-') 
display_value(10,5,'*') 
display_value(10,5,'/') 
display_value(10,5,'%')"""

"""def display_value(a,b,add,sub,multi,div,d):
    if add == '+':
        print(a+b)
    elif sub =='-':
        print(a-b)
    elif multi =='*':
        print(a*b)
    elif div =='/':
        print(a/b)
    elif d == '%':
        print(a%b)
    else:
        print('no')
display_value(10,5,'add','sub','multi','div','d')"""


"""class Person:
    def __init__(self):
     print("hello")
    def cal(self):
        print("hai")
    def value(self):
        print("yes")
    def display(self):
        print("no")    
p = Person()
p.cal() 
p.value() 
p.display()"""

"""class Company:
    def __init__(self):
        print("hello comapny")
    def display(self):
        print("hai")
    def value(self):
        print("have a good day")
    def value1(self):
        print("have a nice day")
company = Company()
company.display()
company.value()
company.value1()"""


"""class Value1:
    def __init__(value,name,ph):
        value.name = name
        value.ph = ph
    def disply(a):
      print(a.name)
      print(a.ph)
h = Value1("ram",12345)
h.disply()"""


"""class Company:
    def __init__(self):
        print("Class started")
    def hi(self,msg):
        print(msg)
c = Company()
c.hi()

c1 = Company()

c2 = Company()
c.hi("hi")
c1.hi("hi")

c2.hi('hi')"""

class Supriya:
    def __init__(value,address,pincode,city):
      print(address,pincode,city)
    def name(value1,cake,flewor,cost):
      print(cake,flewor,cost)
supriya = Supriya("atp",1234,"pamidi")
supriya.name("cake","honey",2000)
s = Supriya("hyderabad",678,"ramoji")


"""class Supriya:
    def __init__(value,address,pincode,city):
      value.address = address
      value.pincode = pincode
      value.city = city
      print(value.address)
      print(value.pincode)
      print(value.city)
    def name(value1,cake,flewor,cost):
      value1.cake = cake
      value1.flewor = flewor
      value1.cost = cost
      print(value1.cake)
      print(value1.flewor)
      print(value1.cost)
supriya = Supriya("atp",1234,"pamidi")
supriya = Supriya("banglore",56789,"karnataka")
supriya.name("cream cake","cream",500)
supriya.name("ice cake","chocolet",1000)"""


"""class Myclass:
    def __init__(value,a,b):
     value.a = a
     value.b = b
     print(a*b)
     print(a/b)
    def value2(value3,c,d):
     print(c+d)
     print(c-d)
a = Myclass(10,20)
a1 = Myclass(5,10)
a.value2(20,30) 
a1.value2(30,40)"""  



"""class Cal:
    name = 'hi'
    def __init__(self):
        pass
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
c = Cal()
c.add(10,20)
c.sub(20,10)"""

"""class Myclass:
    def __init__(self,name,ph):
     print("hai")
     print(name,ph)
c = Myclass("ram",1234)   
c1 = Myclass("sai",5678)""" 







    



