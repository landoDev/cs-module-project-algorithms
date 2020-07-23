'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
    # # Your code here
    # # check how many ways you can eat the cookie
    # # check out how many he ate
    # # small solution
    # # if n == 0:
    # #     return 1
    # # if n < 0:
    # #     return 0
    #     # big solution
    # # if n less than equal to 0
    # if n <= 0:
    #     return 1
    # # if n less than equal to 0
    # if n == 1: 
    #     return 1
    # if n == 2:
    #     return 2
    # if n == 3:
    #     return 4
    # # recursively return each subtree
    # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if this has been calculated by looking in the cache
    elif cache is not None and cache[n] > 0:
        # 2nd base case
        # return the already computed answer and don't recurse
        return cache[n]
    else:
        # have to store value of call expressions in the cache
        if cache is None:
            # initalize empty list for a cache
            cache = [0 for i in range(n+1)]
            # could also do a dictionary
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)  
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
