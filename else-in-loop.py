#
for i in range(5):
    print(i)

else:
    print("its end")    

#
for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("its end")        
#
i=0
while i<5:
    print(i)    
    i=i+1
else:
    print("its end")    


#
for a in range(6):
    print("iteration number {} in for loop".format(a+1))
else:
    print("else in loop")

print("the END")            