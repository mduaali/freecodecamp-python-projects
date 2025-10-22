def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]  # reverse the number to start from the rightmost digit
    odd_digits = card_number_reversed[::2]  # get digits in odd positions (rightmost, every other)

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)  # sum odd digits normally

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]  # get digits in even positions

    for digit in even_digits:
        number = int(digit) * 2  # double the digit
        if number >= 10:
            number = (number // 10) + (number % 10)  # if >=10, add the digits together
        sum_of_even_digits += number  # add to the sum of even digits

    total = sum_of_odd_digits + sum_of_even_digits  # total sum
    return total % 10 == 0  # valid if divisible by 10

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})  # remove dashes and spaces
    translated_card_number = card_number.translate(card_translation)  # clean number

    if verify_card_number(translated_card_number):
        print('valid!')
    else:
        print('invalid!')

main()
