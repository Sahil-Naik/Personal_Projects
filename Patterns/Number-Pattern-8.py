'''

For n=4
Output: (Prints Matrix of NxN containing N as value)

4444
4444
4444
4444

For n=3
Output:

333
333
333

'''

n = int(input())

for i in range(n):
    for j in range(n):
        print(n, end='')
    print()
    
