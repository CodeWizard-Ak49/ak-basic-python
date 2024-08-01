country=("india","russia","brazil","portugal","france")
print(type(country))
print(country)

country1=list(country)
print(type(country1))

country1.append("argentina")
country1.pop(5)
country1[1]="argentina"
country=tuple(country1)
print(country)

all=country+country
print(all)


tup=(0,1,2,3,4,5,6,7,8,9,10)
print(tup.index(4,3,9))