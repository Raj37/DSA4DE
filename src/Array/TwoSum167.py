# Coding pattern- Two Pointers based LeetCode interview questions
# 167. Two Sum II - Input Array Is Sorted | Medium level | Leet Code
# Ref question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=array
# Ref solution: https://www.youtube.com/watch?v=cQ1Oz4ckceM
# Time complexity: O(n)
# Space complexity: no extra space needed- O(1)

# Two sum logic
def two_sum(nums,target):
    left,right=0,len(nums)-1

    while left<right:
        curr_sum=nums[left]+nums[right]

        # if sum of left and right array element > target then move right pointer by 1 pos left to decrease the sum
        if curr_sum>target:
            right-=1

        # if sum of left and right array element < target then move left pointer by 1 pos right to increase the sum
        elif curr_sum<target:
            left+=1

        # as its mentioned clearly in question exactly one solution exits so we will return index of left and right pointers
        else:
            return [left,right]
    return []

if __name__=="__main__":
    arr=[1,3,5,7,10]
    target=10
    print(two_sum(nums=arr,target=target))

