import string


input_string = input("Введіть через дефіс дві літери: ")

letter1, letter2 = input_string.split('-')

letters = string.ascii_letters

start_index = letters.index(letter1)
end_index = letters.index(letter2)

result = letters[start_index:end_index + 1]

print("".join(result))