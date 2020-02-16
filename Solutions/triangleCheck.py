x = int(input("side 1"))
y = int(input("side 2"))
z = int(input("side 3"))

if x == y == z:
	print("Equilateral triangle")
elif x != y != z:
	print("Scalene triangle")
else:
	print("isosceles triangle")