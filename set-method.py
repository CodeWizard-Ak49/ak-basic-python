#set union & union-update
s1={1,2,3,2,4,5}
s2={5,6,7,8,3,1}

print(s1.union(s2))
    #{1, 2, 3, 4, 5, 6, 7, 8}

s1.update(s2)
print(s1)
    #{1, 2, 3, 4, 5, 6, 7, 8}
    
#intersection & intersection_update
s3={"atharv","aditya","anup","raju"}
s4={"raju","ajay","pratik","anup"}

print(s3.intersection(s4))

print(s3.intersection(s4))

#symmetric difference & symmetric difference_update

s5={3,4,5,2}
s6={2,5,6,7}

print(s5.symmetric_difference(s6))

s5.symmetric_difference_update(s6)
print(s5.symmetric_difference_update(s6))

#difference & differenc_update

s7={3,4,5,2}
s8={2,5,6,7}

print(s7.difference(s8))












