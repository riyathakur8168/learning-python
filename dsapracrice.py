# def palindrome(s):

#     left = 0
#     right = len(s) - 1

#     while left < right:

#         if s[left] != s[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# print(palindrome("level"))


def N_fib(n):
    if n==0 or n==1:
        return
    
    return(N_fib(n-1)+ N_fib(n-2)+ N_fib(n-3))

N_fib(4)