from typing import List

## error，可能会导致中位数被跳过
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, r1 = 0, len(nums1)-1
        l2, r2 = 0, len(nums2)-1
        nowpass = 0
        while True:
            m1 = l1 + (r1 - l1) // 2
            m2 = l2 + (r2 - l2) // 2
            mnum1 = nums1[m1]
            mnum2 = nums2[m2]
            
            if mnum1 < mnum2:
                nowpass += m1 - l1 + 1
                l1 = m1 + 1
            elif mnum1 > mnum2:
                nowpass += 0
            
## pass
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 != 0:
            return self.getmink(nums1, nums2, ((m+n)//2)+1)
        else:
            return (self.getmink(nums1, nums2, (m+n)//2) + self.getmink(nums1, nums2, ((m+n)//2)+1))/2
    
    
    def getmink(self, nums1:List[int], nums2:List[int], k):
        l1 = 0
        l2 = 0
        while True:
       
            
            if l1 == len(nums1):
                return nums2[l2+k-1]
            if l2 == len(nums2):
                return nums1[l1+k-1]
            if k == 1:
                return min(nums1[l1], nums2[l2])
            
            p1 = min(l1 + k//2 - 1, len(nums1)-1) 
            p2 = min(l2 + k//2 - 1, len(nums2)-1)
            
            if nums1[p1] <= nums2[p2]:
                k -= (p1 - l1 + 1) ## k变为原来的一半
                l1 = p1 + 1
            elif nums1[p1] > nums2[p2]:
                k -= (p2 - l2 + 1)
                l2 = p2 + 1
    

if __name__=="__main__":
    print(Solution().findMedianSortedArrays([1,3], []))
                
                
            
            
        
            