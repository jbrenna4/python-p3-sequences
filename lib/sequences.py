#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length > 0:
        fib_list.append(0)
        if length > 1:
            fib_list.append(1)
            if length > 2:
                    for i in range(2, length):
                         fib_list.append(fib_list[i - 1] + fib_list[i -2])
    print(fib_list)



