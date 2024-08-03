#format 
string="hi my name is {},i am from {}"
name="athony"
country="brazil"
name2="arnold"
print(string.format(name,country))

#
print(string.format(country,name))

#
string1="hello {1}, where is {0}"
print(string1.format(name,name2))

#f-string

print(f"woow {{country}} is beautiful") #to print value column  

print(f"wake up {name},we are late for over {country} flight")


#using (.2f)

price=3.13999999
print(f"value of PI is {price:.2f}")


print(f"value : {2*4}")


