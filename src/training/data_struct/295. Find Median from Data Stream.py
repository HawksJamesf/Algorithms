'''
295. 数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
'''
import bisect
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_heap = [] #堆顶元素为全堆最大值
        self.large_heap = [] #堆顶元素为全堆最小值
        # heapq.heapify(self.large_heap)
        # heapq.heapify(self.small_heap)

    #时间复杂度O(logn)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.large_heap, num)
        heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))
        if len(self.large_heap) < len(self.small_heap):#large堆 始终比 small堆多一个元素
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))

    def findMedian(self) -> float:
        return (self.large_heap[0]-self.small_heap[0])/2 if len(self.large_heap) == len(self.small_heap) else self.large_heap[0]

class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums=[]

    #时间复杂度O(n)
    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
        else:
            bisect.insort_left(self.nums,num)
    def findMedian(self) -> float:
        if not self.nums:return 0
        n = len(self.nums)
        if n&1:
            return self.nums[n//2]
        else:
            m = n//2
            return (self.nums[m]+self.nums[m-1])/2
if __name__ =='__main__':
    m =MedianFinder()
    m.addNum(1)
    m.addNum(2)
    print(m.findMedian()) #-> 1.5
    m.addNum(3)
    print(m.findMedian()) #-> 2
