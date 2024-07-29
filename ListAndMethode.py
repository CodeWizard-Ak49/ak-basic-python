#list 

atharv=[1,2,3,4,5,6,7,8,9,10]
print(type(atharv))


#for indexing 
print(atharv[3])


#Negative indexing
print(atharv[-3])
print(atharv[len(atharv)-3])


#to know the element present
if 5 in atharv:
    print("true")
else:
    print("false")        

if "ath" in "atharv":
    print("yes")


#jump index
number=[2,4,6,8,10,12,14,16]
print(number[2:7:2])


#list comprehension
list=[i for i in range(5)]
print(list)

list=[i*i for i in range(6)]
print(list)

list=[i for i in atharv if i%2==0]
print(list)