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
    f = sorted(zip(conc, price))
    n = len(f)
    heapf = []
    i = 0
    res = 0
    x = f[0][0]
    while i < n or heapf:
        if not heapf and i < n and x < f[i][0]:  # 堆为空, 没有遍历结束, 下一个function的conc比当前x大
            x = f[i][0]

        while i < n and f[i][0] <= x:
            heapq.heappush(heapf, (-f[i][1], f[i][0]))
            i += 1

        p0, c0 = heapq.heappop(heapf)  # -price, 它的conc
        res += (x-c0) * (-p0)
        x += 1
     
    return res
        #minv, p = heapq.heappop(f) # 弹出当前最小值
        #if f and minv != f[0][0]: # 和下一个是不一样的， 因此
        #    continue
        
        #while f and f[0][0] ==  minv:
        #    res += p  # 加的上一个的p
        #    heapq.heappush(f,(minv+1, p))
        #    _, p = heapq.heappop(f)
        # 当前想要出去，需要的开销，当前最小的x已经定下来了
if __name__ == '__main__':
    fptr= open(os.environ['OUTPUT_PATH'],'a') 
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


'''如果每次都入堆出堆，即：'''
def optimizeReservedConcurrency_BAD(conc,price):  
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

'''复杂度为:
时间复杂度在最坏情况下是：

O(n² log n)

因此在本题约束
n ≤ 10^5
一定会 TLE（超时）。

二、逐步分析你的方法1在干什么

你的代码核心逻辑是：

while f:
    minv, p = heapq.heappop(f)
    if f and minv == f[0][0]:
        res += p
        heapq.heappush(f, (minv + 1, p))

行为本质一句话概括

每次发现一个冲突，就只把其中一个元素 +1，再丢回堆里，反复模拟“单位 +1 操作”

三、复杂度拆解（一步一步）
1️⃣ 排序 + heapify（前置成本）
f = sorted(zip(conc, price))   # O(n log n)
heapq.heapify(f)               # O(n)


👉 这部分没问题，都是可接受的。

2️⃣ while 循环的“真实成本”（关键）

关键在这句：

heapq.heappush(f, (minv + 1, p))


它可能会被执行多少次？

四、最坏情况分析（这是面试官真正关心的）
构造最坏输入
n = 100000
conc = [1, 1, 1, 1, ..., 1]  （全部相同）
price = 任意

最终目标

要让它们变成：

1, 2, 3, 4, ..., n

需要多少次 “+1” 操作？

第1个：+0
第2个：+1
第3个：+2
...
第n个：+(n-1)

👉 总增量次数 =

0+1+2+⋯+(n-1)=n(n-1)/2=O(n^2)

而你的算法是“真的在模拟每一次 +1”

每一次 +1 都会做：

heappop → O(log n)

heappush → O(log n)

👉 单次增量成本 = O(log n)

五、最终时间复杂度推导
部分	复杂度
排序	O(n log n)
heapify	O(n)
单位 +1 操作次数	O(n²)
每次 +1 的堆操作	O(log n)
总复杂度
O(n^2 logn)
六、为什么方法2能过, 而方法1不行?
方法1:
逐步模拟
每 +1 都要堆操作
时间复杂度取决于“最终位移总和”

方法2:
直接计算位移
一次算 (x - c0) * price
每个元素只进堆、出堆一次

👉 方法2复杂度是:
O(nlogn)
'''

'''题目解释：一、题目在说什么？（直观理解）

你在维护一个 serverless 生产系统，里面有 n 个 AWS Lambda 函数。

每个函数 i 有一个当前的 并发上限：conc[i]

如果多个函数并发上限相同，高负载的函数可能会“抢资源”，把别的函数饿死

因此要求：
👉 最终每个函数的并发上限必须两两不同（全部唯一）

二、你能做什么操作？

你只能做一种操作：

对某个函数 i，把 conc[i] 增加 1

但这是有代价的：

每次增加 +1

需要支付 price[i] 的成本

你可以对同一个函数 多次增加

⚠️ 不能减少并发上限，只能增加

三、你的目标是什么？

用最小的总成本，使所有 conc[i] 的值都不相同

最终返回的是：

最小花费（long 类型）'''