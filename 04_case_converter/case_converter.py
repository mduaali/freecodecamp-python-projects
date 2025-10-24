# this function converts a string from camelcase or pascalcase to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # using list comprehension to build a new list of characters
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # join the list into one string and remove any extra underscores at the start or end
    return ''.join(snake_cased_char_list).strip('_')

# alternate version using a for loop for better readability
def convert_to_snake_case_loop(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string

# test both versions
def main():
    print(convert_to_snake_case('aLongAndComplexString'))
    print(convert_to_snake_case_loop('aLongAndComplexString'))

main()
