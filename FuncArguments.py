# #Default argument

def avarage(a=3,b=4):
    print("Avarage : ",(a+b)/2)

avarage()
avarage(a=1,b=2)
avarage()

# #Keyword argument

def name(fname,mname="B",lname="C"):
    print("Hello",fname,mname,lname)

name("A")



def name1(Aname,Bname="2",Cname="3"):
    print("Hello",Aname,Bname,Cname)

name1("1")
#required argument    

def alpha(alpha1,alpha2):
    print("Hello ",alpha1,alpha2)
    #cannot give only 1 argument ,need both argument
alpha(2,3)

   
#variable length argument

def average1(*number):    #(*number) as a tuple
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i 
    print("Average : ",sum/len(number))     

average1(1,2,3,4,5)    


def string(**str):
    print(type(str))
    print("Hello ",str["fname"],str["mname"],str["lname"])

string(lname="C",fname="A",mname="B")