def rotate_array(nums, k):
    n = len(nums)
    k = k % n  
    
    nums.reverse()
    
    nums[:k] = reversed(nums[:k])
    
    nums[k:] = reversed(nums[k:])

    return nums

input_array = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated Array:", rotate_array(input_array, k))
