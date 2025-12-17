'''A new Amazon intern encountered a challenging task, Currently, the intern has n integers, where the value of the i^th element is represented by the array element values[i].The intern is curious to play with arrays and subsequences and thus asks you to join him. Given n integer, array values, and an integer k, the intern needs to find the maximum and minimum median overall subsequences of length k.
Example:
Given n=3, values =[1,2,3],and k=2
Subsequences of length k | median
[1,2] | 1
[1,3] | 1
[2,3] | 2
Here, the maximum median present is 2 and the minimum median in the subsequence present is 1.

Function Description
Complete the function medians in the editor below.
medians has the following parameter(s):
int values[n]: the value of integers. 
int k: the given integer

Returns
int[]: the maximum and minimum overall subsequences of length k in the form [maximum median, minimum median].

Constraints
1≤n≤ 105 
0 ≤ values[i] ≤ 10^9 
1 ≤ k ≤ n

Input Format For Custom Testing
The first line contains an integer, n, denoting the number of elements in values.
Each of the next n lines contains an integer values[i].
The next line contains an integer, k.
'''

import os

if 'OUTPUT_PATH' not in os.environ:
    os.environ['OUTPUT_PATH'] = 'output.txt'

def medians(values, k):
    #Write   your  code  here
    values.sort()
    n = len(values)
    m = (k - 1) // 2  # lower-median index within a sorted subsequence of length k
    min_median = values[m]                 # choose k smallest
    max_median = values[n - k + m]         # choose k largest
    return [max_median, min_median]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    valuescount = int(input().strip())
    values = []
    for _ in range(valuescount):
        values_item = int(input().strip())
        values.append(values_item)
    k = int(input().strip())
    result = medians(values, k)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()