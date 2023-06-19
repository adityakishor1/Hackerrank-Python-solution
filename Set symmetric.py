# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N.symmetric_difference(SET_B)))
