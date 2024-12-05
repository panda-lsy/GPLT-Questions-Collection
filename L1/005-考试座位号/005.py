N = int(input())
id_s,seat0s,seat1s=[],[],[]
for i in range(N):
    '''seat0是试机座位号 seat1是考试座位号'''
    id_,seat0,seat1 = map(int,input().split())
    id_s.append(id_)
    seat0s.append(seat0)
    seat1s.append(seat1)

M = int(input())
check_nums = list(map(int,input().split()))

for num in check_nums:
    print(f'{id_s[seat0s.index(num)]} {seat1s[seat0s.index(num)]}')