import heapq

class MedianFinder:

    def __init__(self):
        self.bigpart = [] ## 小顶堆
        self.smallpart = [] ## 大顶堆

    def addNum(self, num: int) -> None:
        ## 长度相同，是大的部分的长度多1即可
        if len(self.bigpart) == len(self.smallpart):
            if len(self.smallpart) == 0:
                heapq.heappush(self.bigpart, num)
            else:
                maxsmall = - heapq.heappop(self.smallpart)
                if maxsmall <= num:
                    heapq.heappush(self.bigpart, num)
                    heapq.heappush(self.smallpart, -maxsmall)
                else:
                    heapq.heappush(self.bigpart, maxsmall)
                    heapq.heappush(self.smallpart, -num) 
        else:
            minbig = heapq.heappop(self.bigpart)
            if minbig >= num:
                heapq.heappush(self.bigpart, minbig)
                heapq.heappush(self.smallpart, -num)
            else:
                heapq.heappush(self.bigpart, num)
                heapq.heappush(self.smallpart, -minbig)
        
    def findMedian(self) -> float:
        if len(self.smallpart) == len(self.bigpart):
            return (self.bigpart[0] - self.smallpart[0] )/2
        
        else:
            return self.bigpart[0]
