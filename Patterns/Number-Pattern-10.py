'''

For n=4
Output:

4444
333
22
1

'''

n = int(input())
for i in range(n, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end='')
    print()
    
