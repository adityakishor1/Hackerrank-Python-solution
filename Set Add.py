# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
NAMES = set([])
for i in range(n):
    NAMES.add(input())
print(len(NAMES))
