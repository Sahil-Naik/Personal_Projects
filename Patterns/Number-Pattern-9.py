'''

For n=4
Output:

1234
123
12
1

'''

n = int(input())
for i in range(n):
    for j in range(n - i):
        print(j+1, end="")
    print()
    
