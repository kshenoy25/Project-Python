# 1) remove any '-' or ' '
# 2) add all digits in the odd places from right to left
# 3) double every second digit from right to left:
#           (if result is a two-digit number, add the two-digit number together to get a single digit)
# 4) sum the totals of steps 2 & 3
# 5) if sum is divisible by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step 1
# accept some user input

card_number = input("Enter a card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

# reverse string - right to left

card_number = card_number[::-1]
#print(card_number)

# step 2
# need every second digit
for x in card_number[::2]:
    # iterating over a string therefore need a type cast for x
    sum_odd_digits += int(x)

# step 3
for x in card_number[1::2]:
    # doubling every second digit
    x = int(x) * 2
    # if x is a two-digit number
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_odd_digits += x

# step 4

total = sum_odd_digits + sum_even_digits

# step 5

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")

