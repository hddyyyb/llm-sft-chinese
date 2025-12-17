'''on-call 待命 ; 随时待命 ; 随时候召
serverless 无服务器的
concurrency[计] 并发性；同时发生
burst 突发
starve（使）挨饿，饿死；使极其缺乏，需要
incurring 招致（遭受）
provisioned / prəˈvɪʒnd / 预分配的

You're the on-call SDE for a serverless production stack. The architecture includes n AWS Lambda functions, and each function i currently has a reserved-concurrency limit of conc[i]. Because burst load on one function can starve others, your principal engineer asks that every function end up with a distinct concurrency limit.
In one operation you may raise function i's limit by exactly 1, incurring a cost of price[i] (the cost reflects additional provisioned-concurrency dollars).


5
5
2
5
3
3
5
3
7
8
6
9
Example
n = 5
conc = [5,2,5,3,3]
price = [3,7,8,6,9]

An optimal sequence:
Bump function 0 (conc[0]) from 5 ->6 (cost 3).
Bump function 3 (conc[3]) from 3-> 4 (cost 6).

The final limits [6, 2, 5, 4, 3] are all different; total cost = 3 + 6 = 9, which is minimal.

Function Description
The function optimizeReservedConcurrency takes the following inputs:
int conc[n]: the current reserved-concurrency for each lambda
int price[n]: cost to increase that lambda's limit by 1

Returns:
long: the minimum dollars required to make all conc values unique

Constraints
1 ≤n≤10^5 
1≤ conc[i] ≤ 10^9 
1≤ price[i] ≤ 10^5

Input Format for Custom Testing:
The first line contains an integer n, the number of Lambda functions.
Each of the next n lines contains an integer conc[i].
The next line again contains n (the number of functions).
Each of the next n lines contains an integer price[i].
Note: input structure is identical to the previous version of the problem so existing test cases still apply.
'''
import os
import heapq

if 'OUTPUT_PATH' not in os.environ:
    os.environ['OUTPUT_PATH'] = 'output.txt'

def optimizeReservedConcurrency(conc,price):
    #Write your code here

    f = sorted(zip(conc, price))
    heapq.heapify(f)
    print (f)
    res = 0
    while f:
        
        minv, p = heapq.heappop(f) # 弹出当前最小值
        if f and minv == f[0][0]: # 和下一个是一样的
            res += p
            heapq.heappush(f,(minv+1, p))
    
    return res

if __name__ == '__main__':
    fptr= open(os.environ['OUTPUT_PATH'],'w') 
    conc_count = int(input().strip()) 
    conc=[] 
    for _ in range (conc_count ): 
        conc_item = int(input().strip()) 
        conc.append(conc_item) 
    price_count = int(input().strip())
    price=[] 
    for _ in range (price_count ): 
        price_item = int(input().strip()) 
        price.append(price_item)  
    result = optimizeReservedConcurrency(conc,price)
    fptr.write(str(result)+'\n')
    fptr.close()