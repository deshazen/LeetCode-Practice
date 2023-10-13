def merge(nums1, m, nums2, n):
    """
    10/2
    Merge two sorted arrays nums1 and nums2 into nums1
    """

    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    print(nums1)

def removeElement(nums, val):
    """
    removes all occurences of val in nums in place
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1
    print(nums,"::", left)
    return left

def removeDuplicates(nums):
    """
    removes duplicates in a sorted array in place
    returns number of unique elements in nums
    """
    left = 0
    for right in range(1, len(nums)):
        if nums[right] == nums[left]:
            pass
        else:
            left += 1
            nums[left] = nums[right]
    return left + 1

def removeDoubleDupes(nums):
    """
    Removes elements that appear more than twice in a sorted array in place
    returns the number of elements after removal
    """
    if len(nums) <= 2:
        return len(nums)
    left = 2
    for i in range(2, len(nums)):
        if nums[i] == nums[left]:
            pass
        else:
            nums[left] = nums[i]
            left += 1
    return left

def majorityElement(nums):
    """
    returns the majority element in an array
    """
    if len(nums) <= 0:
        return 0
    element = nums[0]
    frequency = 1
    for i in range(1, len(nums)):
        if frequency == 0:
            element = nums[i]
            frequency = 1
        elif nums[i] == element:
            frequency += 1
        else:
            frequency -= 1
    return element

def rotate(nums, k):
    """
    given an integer array nums, rotate the array to the right k steps
    """
    if k > len(nums):
        k = k % len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

def maxProfit(prices):
    """
    returns maximum profit by choosing a single day to buy
     a stock and choosing a different day in the future to sell
    """
    if len(prices) <= 1:
        return 0
    minPrice = prices[0]
    maxProfit = 0
    for i in prices[1:]:
        minPrice = min(minPrice, i)
        profit = i - minPrice
        maxProfit = max(maxProfit, profit)
    return maxProfit

def maxProfit2(prices):
    """
    returns maximum profit by buying and selling stock throughout the prices array
    """
    max_profit = 0
    for i in range(1, len(prices)):
        


nums1 = [7,1,5,3,6,4]
