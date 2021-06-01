# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(0,T):
    S=input()
    N=len(S)
    print(S[0:N:2]+' '+S[1:N:2])
