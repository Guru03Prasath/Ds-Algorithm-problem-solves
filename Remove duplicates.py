def remove_duplicates(nums):
    if not nums:
        return 0
    
    i = 0  
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1


input_array = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(input_array)
print("New Length:", new_length)
