def find_missing_number(arr):
    n = len(arr) + 1  
    total_sum = (n * (n + 1)) // 2  
    array_sum = sum(arr)  
    missing_number = total_sum - array_sum
    return missing_number

input_array = [1, 2, 3, 4, 6, 7, 8]
print("Missing Number:", find_missing_number(input_array))
