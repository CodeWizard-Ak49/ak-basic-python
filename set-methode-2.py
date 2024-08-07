#isdisjoint
s5={3,4,5,2}
s6={2,5,6,7}
    
(print(s5.isdisjoint(s6)))


#issuperset
#issubset
s={1,2,3,4,5,6}
s1={3,2,5,4}

print(s.issuperset(s1))

print(s.issubset(s1))


#add
name={"atharv","aditya","anup","raju"}

name.add("ajay")
print(name)


#remove/discard
#discard do not show error if there is error
#but remove shows error
# name={"atharv","aditya","anup","raju"}

name.discard("atharv")
print(name)

name.remove("ajay")
print(name)

#pop

name1={"atharv","aditya","anup","raju"}

ak=name1.pop()
print(name1)
print(ak)

#del
#clear
'del name1'
'clear ()'





