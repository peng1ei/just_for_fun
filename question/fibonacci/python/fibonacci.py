def fib_iter_v0(n):
    """ Calculate the nth Fibonacci number for with iterative methods.

    version 0

    n -- n = 0, 1, 2, 3, 4, 5, 6, ...

    >>> fib_iter_v0(0)
    0
    >>> fib_iter_v0(1)
    1
    >>> fib_iter_v0(2)
    1
    >>> fib_iter_v0(3)
    2
    >>> fib_iter_v0(8)
    21
    """
    assert n >= 0, 'The n should be greater than or equal to 0.'
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        f_sub_one, f_sub_two = 1, 1 # seed value
        subsequent_num = 0 # subsequent number
        k = 3 # iterative begin

        while k <= n:
            subsequent_num = f_sub_one + f_sub_two
            f_sub_two = f_sub_one
            f_sub_one = subsequent_num
            k += 1
        return subsequent_num

def fib_iter_v1(n):
    """ Calculate the nth Fibonacci for number with iterative methods.

    version 1

    n -- n = 0, 1, 2, 3, 4, 5, 6, ...

    >>> fib_iter_v1(0)
    0
    >>> fib_iter_v1(1)
    1
    >>> fib_iter_v1(2)
    1
    >>> fib_iter_v1(3)
    2
    >>> fib_iter_v1(8)
    21
    """
    assert n >= 0, 'The n should be greater than or equal to 0.'
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        f_sub_one, f_sub_two = 1, 1 # seed value
        k = 3 # iteration begin

        while k <= n:
            f_sub_one, f_sub_two = f_sub_one + f_sub_two, f_sub_one
            k += 1
        return f_sub_one

