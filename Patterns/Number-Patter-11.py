'''
For n=5
Output:

11111
0000
111
00
1

'''

n = int(input())
for i in range(n,0,-1):
    if i%2==0:
        print("0"*i)
    else:
        print("1"*i)
        
