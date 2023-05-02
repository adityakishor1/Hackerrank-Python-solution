if __name__ == '__main__':
    N = int(input())
    L=[];
    for i in range(0,N):
        cmd=input().split();
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop();
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort();
        else:
            L.reverse();
