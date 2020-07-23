'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

    # multiply every element by each other element in a list
    # need to track where the root number is and ignore it while iterating through and multiplying it by all other numbers
    # return the multiplied numbers
    # this has to be close
    # multiplied_arr = [0] * len(arr)
    # resorted to walking through it on leet code, original code is in slack
    length = len(arr)
    # track elements to left and right of the given element
    left, right, multiplied_arr = [0] * len(arr), [0] * len(arr), [0] * len(arr)
    # if there are no elements to the left set index start to 1
    left[0] = 1
    for i in range(1, length):
        # root = arr[i]
        # new_num = 1
        # get the products from the left side of the number
        left[i] = arr[i - 1] * left[i - 1]
    right[length - 1] = 1
    for i in reversed(range(length - 1)):
        # flip it and multiply i by all the elements to it's right
        right[i] = arr[i + 1] * right[i + 1]
    # build the answer array with the multiplied values
    for i in range(length):
        multiplied_arr[i] = left[i] * right[i]
        # filtered_arr = [num for num in arr if num != root]
        # for num in filtered_arr:
        #     new_num = num * new_num
        # multiplied_arr[i] = new_num
    return multiplied_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
