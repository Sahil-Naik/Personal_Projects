'''

For n=4
Output:

1
22
333

'''

n = int(input())
for i in range(n):
    for j in range(i):
        print(i, end='')
    print('')
    
