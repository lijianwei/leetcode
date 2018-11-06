class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens=len(nums)
        i=0
        while i <(lens-1) :
            j=i+1
            while j<=(lens-1):
                if(nums[i]+nums[j]) == target:
                    return [i,j]
                j=j+1
            i=i+1


if __name__ == '__main__':
    solution=Solution()
    result=solution.twoSum([1,2,3,4,5,6], 9)
    print(result)