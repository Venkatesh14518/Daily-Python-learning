# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

for num in range(1500, 2701):      # range(1500, 2701) goes from 1500 to 2700 (2701 is excluded)
    if num % 7 == 0 and num % 5 == 0:   # num % 7 == 0 → divisible by 7, num % 5 == 0 → multiple of 5
        print(num)                # print only the numbers that satisfy both conditions
