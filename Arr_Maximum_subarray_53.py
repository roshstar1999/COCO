def maxSubArray(self, nums: List[int]) -> int:
        start=0
        end=0
        n=len(nums)
        summ=0
        max_sum=nums[0]
        
        #Kadane algo
        
        for i in range(n):
            
            summ+=nums[i]
            if max_sum<summ:
                max_sum=summ
                end=i
            if summ<0:
                start=i+1
                summ=0
        return max_sum
    
