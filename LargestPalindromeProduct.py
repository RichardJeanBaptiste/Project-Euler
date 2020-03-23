'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
def isPalindrome(num):
    forward = 0
    backword = -1
    x = str(num)
    y = int(len(x) / 2)

    for i in range(y):
        if(x[forward] != x[backword]):
            return False
        forward += 1
        backword -=1
    
    return True

largestPalindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        num = i * j
        if(isPalindrome(num)):
            largestPalindrome = num

print(largestPalindrome)
