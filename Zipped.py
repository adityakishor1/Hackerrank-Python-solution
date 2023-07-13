# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = input().split()

io = list()

for _ in range(int(X)):
    ip = map(float, input().split())
    io.append(ip)

for i in zip(*io): 
    print( sum(i)/len(i) ) 
