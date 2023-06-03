'''

For n=5
Output:

*
* *
*  *
*   *
******

'''

n = int(input())
for i in range(1, n+1):
    count = 1
    for j in range(i):
        if j == 0 or j == i-1:
            print('*', end='')
            count += 1
        else:
            if i != n:
                print(' ', end='')
            else:
                print('*', end='')
                count += 1
    print()
    
