class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target 
        # left , right, mid 
        # left = 0, right = nums.length-1 , mid = left+ [(right-left) //2]
        
        # return idx
        
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2   
            #  [1,2,3,4,5]   4,  l =0, r =4, mid = 2, 
            #   [0] 0 , l=r =0, mid =0
            #  [2, 4] 4, l =0, r=1, mid = 0
            if  target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid

        else:
            return -1