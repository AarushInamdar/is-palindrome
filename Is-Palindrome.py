def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # if str(x) == reversed(str(x)):
    #     return True
    # else:
    #     return False
    s = str(x)[::-1]
    print(str(s))

isPalindrome(121)
isPalindrome(2134)
isPalindrome(-113)