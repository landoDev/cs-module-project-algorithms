'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes_legacy(arr):
    # Your code here

    # the zeros need to be moved to the front of the passed array
    # iterate over the arr
    # is there a zero
        # add it to a new array
    # add the two arrays together, zero's in front
    zero_arr = []
    non_zeros = []
    for i in arr: # O(n)
        if i == 0:
            zero_arr.append(i)
        else:
            non_zeros.append(i)
    moved_arr = non_zeros + zero_arr
    return moved_arr

# do this without a new list? 
# need to use pointers
def moving_zeroes(arr):
    # pointers on either side of i 
    # if a left pointer sees a zero and the right pointer sees a non zero, swap those items
    left_index = 0
    right_index = len(arr) - 1
    # loop to iterate 
    # if using sometype of "pointer", use a while loop
    # use a while loop: left <= right
    while left_index <= right_index:
        # if left points at a zero and right isn't zero
        if arr[left_index] == 0 and arr[right_index] != 0:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            # swap values
            # increment left
            left_index += 1
            # decrement right
            right_index -= 1
        # else
        elif arr[left_index] != 0:
            left_index += 1
            # if left isn't zero
                # increment left
        else:
            right_index -= 1
            #if right is zero:
                # decrement right
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")