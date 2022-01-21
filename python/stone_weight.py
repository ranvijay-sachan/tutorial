stone= [5,2,8,1,7,2,8]

[8]
[8]

[5,2,1,7,2]
[7]
[5]

[2,1,2,2]
[2]
[2]
[2,1]
[2]
[1]
[1]



import heapq

def find_stone(stone):
    heap = []
    for s in stone:
        heapq.heappush(heap, -s)
    while len(heap) >= 2:
        print(heap)
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if first != second:
            heapq.heappush(heap, -(first - second))
    if heap:
        return -heap[0]
    return 0

stone= [5,2,8,1,7,1,8]
print(find_stone(stone))      
