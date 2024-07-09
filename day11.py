"""list5=["apple","kiwi","mango","cherry","pomogranet"]
print(list5)
print(list5[3])
list5.append("greps")
print(list5)
list5.insert(3,"banana")
print(list5)
list5.pop(1)
print(list5)
print(list5[2:3])
print(list5[-6:])

list6=["anu","banu","priya","lalli","chinni"]
for name in list6:
    print(name)
print(len(list6))"""

"""list1=["supri","sharu","swapna","deepu","priya"]
print(list1)
list1.append("baru")
print(list1)
list1.insert(4,"kani")
print(list1)
list1.pop(4)
print(list1)
print(list1[2:4])
print (list1[-1])


list2=[1,2,3,4,5,6,7,]
for no in list2:
  if no%2==0:
    print(no)"""

"""class Supriya:
    def __init__(value,cloths,cost):
      print(cloths,cost)
    def number(value1,states,rajadhani):
      print(states,rajadhani)
supriya = Supriya("cotton",30000)
s1 = Supriya("rayon",20000)
s1.number("andhrapradesh","amaravathi")
supriya.number("telngana","hyderabad")"""



"""class Booklibrary:
  def __init__(self):
    self.list_of_books=[]
  def addbook(self,book):
    self.list_of_books.append(book)
    print(self.list_of_books)
  def removebook(self):
    for item in self.list_of_books:
      if item["name"] == "mahabharatha":
       self.list_of_books.remove(item)
  def showbook(self):
   for items in self.list_of_books:
    print(items)
booklibrary = Booklibrary()
booklibrary.addbook({"id":1,"name":"ramayana","athour":"valmiki"})
booklibrary.addbook({"id":2,"name":"mahabharatha","athour":"vedavasya"})
booklibrary.removebook()
booklibrary.showbook()"""

"""class Contactlist:
  def __init__(self):
    self.contact_list=[]
  def addcontact(self,contact):
    self.contact_list.append(contact)
    print(self.contact_list,"added sucessfuly")
  def showcontact(self):
    for item in self.contact_list:
     print(item,"showing items")  
  def removecontact(self):
    self.contact_list.pop(1)
    #for items in self.contact_list:
     #if items["ph"] == 123456:
      #self.contact_list.remove(items)
    print(self.contact_list,"after removing")
c=Contactlist()
c.addcontact({"name":"arjun","ph":123456,"city":"atp"})
c.addcontact({"name":"ram","ph":567889,"city":"bangloor"})
c.addcontact({"name":"laxman","ph":789435,"city":"hyd"})
c.showcontact()
c.removecontact()"""

"""class Ram:
  def __init__(self):
   self.list=[]
   i=1
   while i <= 100:
    print(i)
    self.list.append(i)
    i += 1
  def even(self):
   for i in self.list:
    if i%2==0:
     print("evenn",i)
  def odd(self):
   for i in self.list:
    if i%2!=0:
     print("oddn",i)
ram=Ram()
ram.even()
ram.odd()"""

"""class Contactlist:
  def __init__(self):
    self.contact_list=[]
  def addcontact(self,contact):
    self.contact_list.append(contact)
    print(self.contact_list,"added sucessfuly")
  def showcontact(self):
    for index,item in enumerate(self.contact_list):
     print(index,item,"showing items")  
  def removecontact(self,name):
    for index,items in enumerate(self.contact_list):
     if name == items["name"]:
      print(index,name)
      self.contact_list.pop(index)
c=Contactlist()
c.addcontact({"name":"arjun","ph":123456,"city":"atp"})
c.addcontact({"name":"ram","ph":567889,"city":"bangloor"})
c.addcontact({"name":"laxman","ph":789435,"city":"hyd"})
c.showcontact()
c.removecontact("arjun")
c.showcontact()"""



"""class Book:

  def __init__(self):
    self.listofbooks=[]

  def addbook(self,book):
    self.listofbooks.append(book)
    print(self.listofbooks,"add successfully")
  
  def removebook(self,name):
   for index,item in enumerate(self.listofbooks):
    if name == item["name"]:
       print(index,item,"removing")
       self.listofbooks.pop(index)

  def showbook(self):
    for index,item in enumerate(self.listofbooks):
     print(index,item,"showin items")

  def showingbook(self,id):
    for index,item in enumerate(self.listofbooks):
     if id == item["id"]:
       print(index,item,"showing items")

  def updatebook(self,name):
    for index,item in enumerate(self.listofbooks):
      if name == item["name"]:
        item.update({"name":"c++"})  
        print(index,item,"update items")
  def updateb(self,id,val,key,value):
    for item in self.listofbooks:
        if id == item["id"]:
          item.update({"id":val,key:value})
          print(item,"ubdateitems") 
  def upd(self,name,key,values):
    for item in self.listofbooks:
      if name == item["name"]:
        item.update({key:values})
        print(item,"ubdate")
b=Book()
b.addbook({"id":1,"name":"java","athour":"jemsgosling"}) 
b.addbook({"id":2,"name":"python","athour":"abcd"}) 
b.addbook({"id":3,"name":"c","athour":"jems"}) 
b.addbook({"id":4,"name":"aws","author":"sdf"})
b.showingbook(3)
b.showbook()  
b.removebook("python") 
b.showbook()
b.showingbook(2) 
b.updatebook("aws")
b.updateb(3,6,"name","cloud computing")
b.upd("c++","id",89)"""


"""class Main:
  def __init__(self):
    self.listofnames = []
    self.id = 1
  def addname(self,names):
    names.update({"id":self.id})
    self.id += 1
    self.listofnames.append(names)
    print(self.listofnames)
  def updates(self,id,value,key,values):
    for i in self.listofnames:
      if id == i["id"]:
        i.update({"id":value,key:values})
        print(i,"ubdate")
  def ub(self,name):
    for i in self.listofnames:
      if name == i["name"]:
        print(i,"ub")
main = Main()
main.addname({"name":"ram","athour":"ert"})
main.addname({"name":"sam","athour":"fghj"})
main.addname({"name":"laxman","athour":"xcv"})
main.updates(1,7,"name","arjun")
main.ub("laxman")"""


class Movies:
  def __init__(self):
    self.listofmovies=[]
    self.id = 1
  def addname(self,movie):
    movie.update({"id":self.id})
    self.listofmovies.append(movie)
    print(self.listofmovies)
    self.id += 1
  def removename(self,id):
    for index,i in enumerate(self.listofmovies):
      if id == i["id"]:
        self.listofmovies.pop(index)
        print(index,self.listofmovies,"removing")
  def ubdatename(self,name,value,key,values):
    for i in self.listofmovies:
      if name == i["name"]:
        i.update({"name":value,key:values})
        print(i,"ubdates")
  def accesname(self,id):
    for i in self.listofmovies:
      if id == i["id"]:
        print(i,"acces")

movies = Movies()
movies.addname({"name":"shivam","hero":"ram"})
movies.addname({"name":"khusi","hero":"pavan"})
movies.addname({"name":"kalki","hero":"brabhas"})
movies.removename(1)
movies.ubdatename("khusi","khu","hero","kalyan")
movies.accesname(2)





