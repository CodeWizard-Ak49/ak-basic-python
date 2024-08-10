try:
    Q=[1,2,3,4,5]
    i=int(input("enter the index number :"))
    print(Q[i])

except:
    print("some error occurred")

finally:
    print("run at any cost")   

def try1():
 try:
   X=[2,4,6,8,10]
   Y=int(input("take no. :"))
   print(X[Y])
   return 1
 except:
   print("error occurred")
   return 0

 finally:
   print("print anyway") 


x=try1()
print(x)


   
   

       
       
  


