# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it

count_primes = 0                          # variable to count how many primes we find

for num in range(2, 101):                 # primes start from 2 up to 100
    is_prime = True                       # assume the number is prime unless proven otherwise

    for divisor in range(2, int(num**0.5) + 1):   # check divisors from 2 to sqrt(num)
        if num % divisor == 0:            # if num is divisible, it's NOT prime
            is_prime = False
            break                          # stop checking further

    if is_prime:                          # if still True, the number is prime
        print(num)                        # print the prime number
        count_primes += 1                 # increase count

print("Total prime numbers between 0 and 100:", count_primes)   # final count
