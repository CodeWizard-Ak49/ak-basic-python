list=[3,2,5,6,8,1,4,9,1]
print(list)

#append i.e add at end
list.append(10)
print(list)

#sort ~ assending
list.sort()
print(list)

list.sort(reverse=True)
print(list)

#find index
print(list.index(4))
print(list.count(1))

List=list.copy()
List[0]=0
print(list)
print(List)

list.insert(5,22)
print(list)

