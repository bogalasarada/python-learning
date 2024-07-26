"""class Flowers:
    def __init__(self):
        self.listofflowers = []
        self.id = 1
    def addflowers(self,flower):
        flower.update({"id":self.id})
        self.listofflowers.append(flower)
        print(self.listofflowers,"adding flowers")
        self.id += 1
    def updateflower(self,name,value):
        for i in self.listofflowers:
            if name == i["name"]:
                i.update({"name":value})
                print(i,"updatating flower")
    def removeflower(self,id):
        for index,i in enumerate(self.listofflowers):
            if id == i["id"]:
                self.listofflowers.pop(index)
                print(index,i,"removing flower")
    def showingflowers(self):
        for index,i in enumerate(self.listofflowers):
            print(index,i,"showingflowers")
    def showflower(self,id):
        for i in self.listofflowers:
            if id == i["id"]:
                print(i,"show flower")
flowers = Flowers()
flowers.addflowers({"name":"jasmin","cost":50})
flowers.addflowers({"name":"rose","cost":20})
flowers.addflowers({"name":"lilly","cost":100})
flowers.addflowers({"name":"lotus","cost":60})
flowers.addflowers({"name":"sunflower","cost":200})
flowers.updateflower("rose","whiterose")
flowers.showingflowers()
flowers.showflower(3)
flowers.removeflower(4)"""

"""def add(a,b):
    c = a+b
    return c
result = add(10,20)
print(result)
r = result+10
print(r)"""

"""class Main:


    def __init__(self):
        self.listofnames = []
        self.id = 1

    def addnames(self,name):
        name.update({"id":self.id})
        self.listofnames.append(name)
        self.id += 1
        return self.listofnames,"added sucessfully"
    
    def removenames(self,id):
        for index,i in enumerate(self.listofnames):
            if id == i["id"]:
                self.listofnames.pop(index)
                return index,i,"removing"
            
    def shownames(self):
        for i in self.listofnames:
            return self.listofnames,"showing items"
        
    def updatenames(self,name,value):
        for i in self.listofnames:
            if name == i["name"]:
                i.update({"name":value})
                return i,"update"
            
main = Main()
a = main.addnames({"name":"ram"})
a = main.addnames({"name":"laxman"})
a = main.addnames({"name":"bharath"})
a = main.addnames({"name":"shathrugn"})
e = main.removenames(1)
g = main.shownames()
f = main.updatenames("laxman","lucky")
print(a)
print(e)
print(g)
print(f)"""

"""class Voting:
    def __init__(self):
        self.vote = "hai voting"
        self.count = 0
        self.counts = 0
        self.voting = []
        self.voting1 = []
        self.voting2 = []
        self.total = 0
        self.totals = 0
        self.votingmichen = [{"name":"a","candidate":100,"total":0},{"name":"b","candidate":200,"total":0}]
    
        
    def allowingvoter(self,voter):
        result = self.checkingelgibility(voter["age"])
        result1 = self.checking(voter["id"])
       # self.check(voter["candidate"])
        if result1 == True:
            print("thank you voted,we have already voted")
            self.voting2.append(voter)
            print(self.voting2)
            return
       
        if result == True:
            print("allowing the voter")
            self.count += 1
           
            self.voting.append(voter)
           
            self.check(voter['candidate'])
        
        
        
        if result == True:
            print(self.voting)
            return

       
        else:
            print("donot allow the voter")
            self.counts +=1
          
            self.voting1.append(voter)
           
            
    def checkingelgibility(self,age):
        if age >= 18:
            return True
        else:
            return False
    def checking(self,id):
        for i in self.voting:
            if id == i["id"]:
              return True
        return None
    def check(self,candidate):

        for i in self.votingmichen :
           if candidate == i["candidate"]:
               total = i['total']+1
               i.update({'total':total})

               # print(self.votingmichen)
        print(self.votingmichen)
    def victory(self):
        print(self.votingmichen)
   


voting = Voting()
voting.allowingvoter({"name":"ram","age":21,"id":1,"candidate":200})
voting.allowingvoter({"name":"krishna","age":20,"id":2,"candidate":200}) 
voting.allowingvoter({"name":"arjun","age":20,"id":3,"candidate":100})  
voting.allowingvoter({"name":"bharath","age":24,"id":4,"candidate":100}) 
voting.allowingvoter({"name":"raj","age":21,"id":5,"candidate":200})
voting.victory()"""


"""a = [{"name":"ram","id":1,"total":10},{"name":"raj","id":2,"total":0}]
for i in a:
     i.update({"total":i['total']+1})
print(a)"""

"""class Voting:
    def __init__(self):
        self.votingmichen = [{"name":"ysr","candidate":"fan","total":0},{"name":"tdp","candidate":"cycle","total":0},{"name":"janasena","candidate":"glass","total":0}]
        self.vote = []
        self.vote1 = []
    def votingeligibility(self,age):
        if age >= 18:
            return True
        else:
            return False
    def duplicationvoter(self,id):
        for i in self.vote:
            if id == i["id"]:
                return True
        return None
    def candidatevoting(self,candidate):
        for i in self.votingmichen:
            if candidate == i["candidate"]:
                total = i["total"]+1
                i.update({"total":total})  
    def victory(self):
        for i in self.votingmichen:
            if i["total"] > i["total"]:
                print("win")       
    def totalvotes(self):
        print(self.votingmichen)
    def allowingvoter(self,voter):
        result = self.duplicationvoter(voter["id"])
        result1 = self.votingeligibility(voter["age"])
        if result == True:
            print("thanks for voting we have alredy voted")
            return
        if result1 == True:
            print("please allowing the voter")
            self.vote.append(voter)
            self.candidatevoting(voter["candidate"])
        else:
            print("don't allow the voter")
            self.vote1.append(voter)
v = Voting()
v.allowingvoter({"name":"sharada","id":1,"age":23,"candidate":"fan"})
v.allowingvoter({"name":"sunil","id":2,"age":21,"candidate":"fan"})
v.allowingvoter({"name":"deepthi","id":3,"age":24,"candidate":"fan"})
v.allowingvoter({"name":"raghu","id":4,"age":30,"candidate":"cycle"})
v.allowingvoter({"name":"sharada","id":1,"age":23,"candidate":"fan"})
v.allowingvoter({"name":"kanish","id":5,"age":3,"candidate":"fan"})
v.allowingvoter({"name":"supriya","id":6,"age":23,"candidate":"glass"})
v.totalvotes()
v.victory()"""

"""list1 = ['a','b','c','c','c','a','d']
count = 0
count1 = 0
count2 = 0
count3 = 0
for i in list1:
    if i == 'a':
        count += 1
    if i == 'b':
        count1 += 1
    if i == 'c':
        count2 += 1
    if i == 'd':
        count3 += 1
        print(count,'a',count1,'b',count2,'c',count3,'d')"""

"""list = ['a','b','a','c','c','a']
count = 0
for items in list:
    if items == 'c':
        count += 1
        print(count)"""

"""a = [1,2,3,4,5,6,7,8,9,10]
evenlist = []
oddlist = []
for i in a:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
for i in evenlist:
    print(i)
for i in oddlist:
    print(i)"""

"""a = [1,2,6,7,8,9,10,3,4]
sum = 0
totalsum=0
for i in a:
    sum = sum + i
for i in range(1,11):
     totalsum = totalsum + i
print(totalsum - sum)"""

"""sum = 0
for i in range(1,51):
    sum = sum + i
print(sum)"""

"""sum = 0
for i in range(1,21):
    if i % 2 == 0:
        sum = sum + (i*i)
print(sum)"""

"""height = [3.2,3.3,3.1,3.5,3.6,3.7,3.8,3.9]
sortedheight = sorted(height)
for i in sortedheight:
   print(i)"""

"""salary = [10,4,6,7,8,3,2,12]
average_salary = sum(salary) / len(salary)
print(average_salary)"""


"""temp = float(input("ENTER THE TEMPERATURE: "))
fahrenheit = (9/5)*temp + 32
print(fahrenheit)"""

"""a = [80,60,90,70,50]
for i in a:
    if i >= 90:
        print("excellent")
    if i >= 70:
        print("good")
    if i >= 50:
        print("poor")"""

rev  = 0
num = 142
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)





    

        






            

   

    




    
    