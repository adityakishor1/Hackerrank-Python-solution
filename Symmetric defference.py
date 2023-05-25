# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    M = int(input().strip())
    set_m = set(map(int, input().strip().split(' ')))
    
    N = int(input().strip())
    set_n = set(map(int, input().strip().split(' ')))
    
    for j in sorted(set_m ^ set_n):
        print(j)
