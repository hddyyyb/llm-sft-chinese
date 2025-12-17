import os

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