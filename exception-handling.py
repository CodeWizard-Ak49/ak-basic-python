a=input("enter the numder for table :")
print(f"multiplication table of '{a}' is :")

try:
  for i in range(1,11):
    print(f"{int(a)} X {i} ={int(a)*i}")

except Exception as e:
   print("'there is error'")

print("here is end of code")   
print("''thank you''")

try:
  num=int(input("enter the integer number : "))
  a=[2,3]
  print(a[num])

except ValueError:
  print("entered number is not integer")
except IndexError:
  print("index error")

  