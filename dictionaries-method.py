roll={11:"ad",12:"dd",23:"ss"}
roll2={12:"ak",14:"df",22:"sh"}

roll.update(roll2)
print(roll)

roll.clear()

print(roll)

roll2.pop(12)
print(roll2)

roll2.popitem()
print(roll2)

del roll2[14]
print(roll2)