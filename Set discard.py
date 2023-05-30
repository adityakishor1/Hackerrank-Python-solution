n = int(input())
s = set(map(int, input().split())) # Set of n elements

for i in range(int(input())): # Iterate in range of the input num
    s1 = input().split()
    if s1[0] == 'pop':
        s.pop()
    elif s1[0] == 'remove':
        s.remove(int(s1[1]))
    elif s1[0] == 'discard':
        s.discard(int(s1[1]))

print(sum(s))
