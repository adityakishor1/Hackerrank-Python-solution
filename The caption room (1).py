# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
ROOM_LIST = input().split()
ROOM_SET = set(ROOM_LIST)

for ele in list(ROOM_SET):
    ROOM_LIST.remove(ele)

CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
print(CAPTAIN_ROOM_NUM)
