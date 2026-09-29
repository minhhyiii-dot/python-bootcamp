#Write a program that generates the Collatz sequence for a starting number of 20. The sequence updates based on the current number: if the number is even, the next number is exactly half of it. If it is odd, the next number is three times the current number plus one. This process repeats dynamically, and the sequence must terminate the moment the number reaches 1.
#Print every number in the sequence as it evaluates (including the starting 20). Ensure all numbers remain standard integers, not floats. When the sequence finally ends, print EXACTLY: "Sequence complete".
n = 20
while n > 1:
    if n % 2 == 0:
        print(int(n))
        n = n / 2
    else:
        print(int(n))
        n = 3*n + 1
print("Sequence complete")