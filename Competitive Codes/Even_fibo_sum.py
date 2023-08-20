def fibon(limit):
    final_sum = [1,1]
    while sum(final_sum[2::]) < limit+1:
        final_sum.append(final_sum[-1]+final_sum[-2])
     
    #print("Current Series: {}".format(final_sum))
    result = 0
    for j in final_sum:
        if j%2==0:
            #print(j)
            result+=j
    return print(result)

fibon(10)

'''
Problem: Find the sum of Even Fibonacci series numbers less that N

Input: 10
Output: 10
In this case we get series as [0,1,1,2,3,5,8]
Getting sum of even numbers, i.e. 2+8 = 10

Input: 100
Output: 44
'''
