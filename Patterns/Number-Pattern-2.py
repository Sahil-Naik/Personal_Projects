'''

For n=4
Output:

1
11
202
3003

'''

n = int(input())

for i in range(n):
    if i<2:
        print('1'*(i+1))
    else:
        print("{}{}{}".format(i,'0'*(i-1),i))
        
