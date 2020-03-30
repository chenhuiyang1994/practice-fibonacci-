import numpy as np
import sys
def fact(n):
    if (n==0):
        return 1;
    else:
        return n * fact(n-1);

a = fact(5);

memory = [0] * 100000;

def fib(n):
    if n <= 1:
        return n;
    if memory[n] != 0:
        return memory[n];
    memory[n] = fib(n-1) + fib(n-2);
    return memory[n];

b = fib(7);
print (b);

def fib_sum(n):
    if n<=1:
        return fib(n);
    else:
        return fib(n)+fib_sum(n-1);

c = fib_sum(7);
print(c);
