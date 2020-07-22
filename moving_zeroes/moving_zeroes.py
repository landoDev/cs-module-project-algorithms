'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # the zeros need to be moved to the front of the passed array
    # iterate over the arr
    # is there a zero
        # add it to a new array
    # add the two arrays together, zero's in front
    zero_arr = []
    non_zeros = []
    for i in arr:
        if i == 0:
            zero_arr.append(i)
        else:
            non_zeros.append(i)
    moved_arr = zero_arr + non_zeros
    return moved_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")