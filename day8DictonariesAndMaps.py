# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phone_book = dict(input().split() for _ in range(n))
while True:
    try:
            
        queries=input()
        if queries in phone_book :
            print(queries+"="+str(phone_book[queries]))
        else:
            print('Not found')
    except:
        break    
