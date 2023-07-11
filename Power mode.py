# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = int(input())
b = int(input())
m = int(input())

c = math.pow(a, b)
d = c%m

print(int(c))
print(int(d))
