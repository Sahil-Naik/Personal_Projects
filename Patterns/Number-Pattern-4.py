'''

For n=4
Output:

1
22
333
4444

'''

n = int(input())

for i in range(n):
    for j in range(i+1):
        print(i+1,end='')
    print()
    
