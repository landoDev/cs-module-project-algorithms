'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # use recursion to make a binary tree
    # the amount of cookies has an index ( is a list )
    # I can eat the index from left to right, call eat cookies recursively until there are no cookies left
    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
