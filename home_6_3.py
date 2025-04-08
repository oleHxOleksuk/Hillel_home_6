number = int(input("Введіть ціле число: "))

while number > 9:
    digits = [int(digit) for digit in str(number)]
    product = 1
    for digit in digits:
        product *= digit
    number = product

print(number)



