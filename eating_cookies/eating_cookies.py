'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # use recursion to make a binary tree
    # the amount of cookies has an index ( is a list )
    # I can eat the index from left to right, call eat cookies recursively until there are no cookies left
    
    # check how many ways you can eat the cookie
    # check out how many he ate
    # if n less than equal to 0
    if n <= 0:
        return 1
    # if n less than equal to 0
    if n == 1: 
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    # recursively return each subtree
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
