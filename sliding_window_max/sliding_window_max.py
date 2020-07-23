'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # arr 
    # initiate largest values
    largest = []
    # start index
    start = 0 
    # the end = k
    end = k
    # while the end - 1 < than length of nums
    while end - 1 < len(nums):
        #current values = # nums[start index: end index]
        current = nums[start:end]
        # call max for largest values
        largest.append(max(current))
        # increment indices by 1
        start += 1
        end +=1
    # return largest values
    return largest




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
