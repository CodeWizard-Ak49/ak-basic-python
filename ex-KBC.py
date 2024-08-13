k="''' WELCOME TO KON BANEGA KARODPATI '''"
print(k.center(150))

name=input("Enter Your Name : ")
print(f"\nWelcome {name}...!")
start="''' LET'S START '''"
print(start.center(150))

questions=[["Which is the largest planet in our solar system?","Earth","Mars","Jupiter","Saturn",3],["Which is the longest river in the world?","Nile","Amazon","Ganges","Yangtze",1],["Which of the following is a primary color?","Green"," Yellow","Purple","Blue",4],["What is the capital city of Australia?","Sydney"," Melbourne","Canberra","Perth",3],["Who wrote the Indian national anthem?","Bankim Chandra Chattopadhyay","Sarojini Naidu"," Rabindranath Tagore","Subramania Bharati",3],["What is the chemical symbol for water?","O2","CO2","H2O","NaCl",3],["Which continent is the Sahara Desert located in?","Asia","Africa"," Australia","South America",2],["Who was the first man to walk on the moon?","Yuri Gagarin","Neil Armstrong"," Buzz Aldrin","Michael Collins",2],["What is the main ingredient in traditional Japanese sushi?","Beef","Chicken","Rice","Noodles",3],["Which is the national sport of Canada?","Ice Hockey","Baseball","Cricket","Football",1],["Which is the largest organ in the human body?","Heart","Liver","Skin","Lungs",3]]

levels=[1000,3000,5000,8000,12000,25000,100000,175000,300000,700000,2100000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\nQuestion for level Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"1. {question[1]}     2. {question[2]}")
    print(f"3. {question[3]}     4. {question[4]}")
    reply=int(input("\nEnter Your Answer OR 0 to Quit:"))
    if(reply==0):
        money=levels[i-1]
    if(reply==question[-1]):
        print(f"Correct Answer,You won the Rs.{levels[i]}")
        if(i==2):
            money=5000
        elif(i==5):
            money=25000
        elif(i==8):
            money=300000
        elif(i==10):
            money=2100000
    else:
        print("Wrong Answer")
        break    
win=(f"CONGRATULATIOS... {name}...")
if(i==10):
    print(win.center(150))
print(f"\nYour take home money is '{money}'\n\n")    