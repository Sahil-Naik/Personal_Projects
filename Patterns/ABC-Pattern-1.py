'''
For n=4
Output:
A
AB
ABC
ABCD
'''

n = int(input())

for i in range (65,65+n):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()
    
