'''

For n=5
Output:

E
DE
CDE
BCDE
ABCDE

'''
n = int(input())

for i in range(64+n,64,-1):
    k = i
    while k!=(65+n):
        print(chr(k),end='')
        k+=1
    print()
    
