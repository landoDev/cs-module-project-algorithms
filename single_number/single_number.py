'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # return a list
    # needs to iterate over
    # needs to check if there is a duplicate in that list

    # for each number, have you seen it more than once in the list?
        # if so, keep going
        # otherwise, return it

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")