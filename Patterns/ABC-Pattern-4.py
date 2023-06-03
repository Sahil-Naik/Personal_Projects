'''

For n=3
Output: (Prints NxN matrix contain alphabet upto n place)

ABC
ABC
ABC

For n=4
Output:

ABCD
ABCD
ABCD
ABCD

'''

n = int(input())


for i in range(n):
    for j in range(65, 65+n):
        print(chr(j), end='')
    print()
    
