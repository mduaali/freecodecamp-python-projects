# function using a for loop
def convert_to_snake_case_loop(pascal_or_camel_cased_string):
    # create an empty list to store converted characters
    snake_cased_char_list = []

    # loop through each character in the string
    for char in pascal_or_camel_cased_string:
        # if uppercase, add an underscore and convert to lowercase
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        # if not uppercase, add the character as is
        else:
            snake_cased_char_list.append(char)

    # join the list into a single string
    snake_cased_string = ''.join(snake_cased_char_list)

    # remove any underscores that might appear at the beginning or end
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string


# function using list comprehension
def convert_to_snake_case_list_comprehension(pascal_or_camel_cased_string):
    # build the snake case string with list comprehension
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # join and strip underscores
    return ''.join(snake_cased_char_list).strip('_')


def main():
    # test string
    test_string = 'aLongAndComplexString'

    print('loop version:', convert_to_snake_case_loop(test_string))
    print('list comprehension version:', convert_to_snake_case_list_comprehension(test_string))


main()
