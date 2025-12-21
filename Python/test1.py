# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b   


text1 = 'Hello'
text2 = 'World'
## message = '{} {}!'.format(text1, text2) <-- Old way

## Using f-strings (Python 3.6+)

message = f'{text1} {text2}!' ## <-- New way

print(f"\n{message}")

## Looping through a list with indexes
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
