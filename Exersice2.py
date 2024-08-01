hello="Hello Chief"
print(hello.center(50,"_"))

print("what's up?")
print("1-good  2-not good")
print(" ")
ans=int(input("Ans:"))


if ans==1:
    print("Greate")
else:
    print("all is well")  
print(" ")      

# print("today time is :")
print("want to know the time?")
import time
real2=time.strftime('%H:%M:%S')
print("its ",real2)

real1=int(time.strftime('%H'))
print(real1)
if(real1>=0 and real1<12):
    print("good morning")
elif(real1>=12 and real1<17):
    print("good afternoon")
elif(real1>=17 and real1<19):
    print("good evening")
elif(real1>=19 and real1<23):
    print("good night")    
        
    



