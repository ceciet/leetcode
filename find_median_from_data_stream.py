import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_list = []
        self.max_list = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.max_list) == len(self.min_list):
            n = heapq.heappushpop(self.max_list, (-num, num))
            heapq.heappush(self.min_list, n[1])
        else:
            n = heapq.heappushpop(self.min_list, num)
            heapq.heappush(self.max_list, (-n, n))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """

        if self.min_list == []:
            return
        if len(self.max_list) == len(self.min_list):
            return (self.max_list[0][1] + self.min_list[0])/2.0
        return self.min_list[0]
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

if __name__ == "__main__":
    #addNum(-1),findMedian(),addNum(-2),findMedian(),addNum(-3),findMedian(),addNum(-4),findMedian(),addNum(-5),findMedian()
    #addNum(6),findMedian(),addNum(10),findMedian(),addNum(2),findMedian(),addNum(6),findMedian(),addNum(5),findMedian(),addNum(0),findMedian(),addNum(6),findMedian(),addNum(3),findMedian(),addNum(1),findMedian(),addNum(0),findMedian(),addNum(0),findMedian()
    s = MedianFinder()
    s.addNum(6)
    print s.findMedian()
    s.addNum(10)
    s.addNum(2)
    print s.min_list
    print s.max_list
    print s.findMedian()
    s.addNum(6)

    print s.findMedian()