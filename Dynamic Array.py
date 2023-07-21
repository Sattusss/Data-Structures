import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    lastAnswer = 0
    seqList = [[] for _ in range(n)]
    result = []
    for query in queries:
        if query[0] == 1:
            seq = (query[1] ^ lastAnswer) % n
            seqList[seq].append(query[2])
        else:
            seq = (query[1] ^ lastAnswer) % n
            lastAnswer = seqList[seq][query[2] % len(seqList[seq])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    