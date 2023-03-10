class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Method 1 
        # Time complexity of O(n)
        # ans=[]
        # n=len(nums)
        # for i in range(len(nums)):
        #     if nums[i]%2==0:
        #         ans.append(nums[i])
        # for i in range(len(nums)):
        #     if nums[i]%2!=0:
        #         ans.append(nums[i])
        # return ans
        
        # Method 1 with different Code
        # return [i for i in nums if i%2==0] + [i for i in nums if i%2 !=0]
        
        # Method 2
        # i=0
        # j=len(nums)-1
        # while i <j:
        #     while nums[i]%2 !=0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         j -=1
        #         if j<=i:
        #             break
        #     i +=1
        # return nums
        # Method 2 with little-bit dfferent code
        i=0
        j=len(nums)-1
        while i <j:
            if nums[i]%2 !=0:
                nums[i],nums[j]=nums[j],nums[i]
                j -=1
            else:
                i +=1
        return nums
                