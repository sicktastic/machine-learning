# recursion in python

# divide-and-conquer or decrease-and-conquer
#   - reduce a problem to simpler versions of the same problem

# programming technique where a function calls itself
#   - in programming, goal is to NOT have infinite recursion
#       - must have 1 or more base cases that are easy to solove

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# a * b
# a + a (b - 1)
def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)

# recursive function scope example

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(4))


# iteration vs recursion

# iteration

def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

# recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# example of induction
# 0 + 1 + 2 + 3 + ... + n = (n(n + 1)) / 2

# https://www.youtube.com/watch?v=WPSeyjX1-4s
# 23:16

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)

    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        and = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
