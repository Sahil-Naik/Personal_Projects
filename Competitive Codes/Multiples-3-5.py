def sum_multi(num):
    final_sum = 0
    for i in range(0,num):
        if i%3==0 or i%5==0:
            final_sum += i
    print(final_sum)
    
sum_multi(10)

'''
Input: 10
Output: 23

Problem: Find the sum of numbers that are divisible by either 3 or 5 that are less than 10
In this case we get 3+5+6+9 = 23

Similarly for,
Input: 100
Output: 2318
'''
