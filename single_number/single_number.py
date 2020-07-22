'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # return a list
    # needs to iterate over
    # needs to check if there is a duplicate in that list
    number = None
    # iterate over the original array
    for i in arr:
        # check each number against the original array and see if it occurs again
        index = i
        occurences = 0
        for num in arr:
            if index == num:
                occurences += 1
        if occurences < 2:
            number = index
            return number
            # if it does, increment the occurence
        # if that number has more than one occurrence, keep going, otherwise return that number
    return number



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")