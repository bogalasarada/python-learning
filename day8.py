n = [1,2,3,4,5,6,7]
m = []
for item in n:
    m.append(item)
print(m)
    


n1 = [8,9,3,1,2,0,5,0]
zero = []
num = []
for items in n1:
    if items == 0:
     zero.append(items)
    else:
        num.append(items)
print('zeros:',zero)
print('numbers:',num)



#n2 = [8,9,3,1,2,0,5,0]
#for i in n2:
   # n2.append(i)
    #print(i)



'''tuple1 = ("ram","seetha","lakshman")
for fruits in tuple1:
 print(fruits)'''


names = ("ram","seetha","lakshman")
m = list(names)
m.append("oormila")
print(m)
f = tuple(m)
print(f)

n3 = ('a',)
print(n3)
        

    
