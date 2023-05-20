# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
