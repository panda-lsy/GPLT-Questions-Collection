N,sign=input().split()
N=int(N)
for i in range(int(N//2)):
    print(sign*N)
if N/2-N//2>=0.5:
    print(sign*N)