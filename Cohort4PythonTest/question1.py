# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
import math
# (x1, y1 coordinates)
x1 = int(input("Enter the x1 coordinate: "))
y1 = int(input("Enter the y1 coordinate: "))

# (x2, y2 coordinates)
x2 = int(input("Enter the x2 coordinate: "))
y2 = int(input("Enter the y2 coordinate: "))

distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(f"The distance between coordinates of (x1, y1) and (x2, y2) is {distance:.2f}")





# Question 1(ii)
# Write a Python program to find maximum between three numbers.

numbers = [4, 8, 50]

maximum_value = max(numbers)
print(maximum_value)





