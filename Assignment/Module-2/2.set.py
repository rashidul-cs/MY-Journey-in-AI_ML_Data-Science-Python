
def setfunction(set1=set(), set2=set()):
  
  set_union = set1 | set2

  set_intersection = set1 & set2

  set_difference = set1 - set2

  return set_union, set_intersection, set_difference



user_input1 = input("Input for first Set, write here with Comma: ")

setA = set(map(int, user_input1.split(","))) if user_input1.strip() else set()

user_input2 = input("Input for first Set, write here with Comma: ")

setB = set(map(int, user_input2.split(","))) if user_input2.strip() else set()

u, i, d = setfunction(set1=setA, set2=setB)

print(f"Set A: {setA}")
print(f"Set B: {setB}")
print(f"Union: {u}")
print(f"Intersection: {i}")
print(f"Difference (set1 - set2): {d}")
