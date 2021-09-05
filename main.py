
end_program = "N"


while end_program != "Y":

    noun_to_plural = input("Welcome to the plural convertor, enter your noun "
                           "to convert it to plural: ")

    if noun_to_plural[-1] == 'x':
            noun_to_plural += 'es'

    elif noun_to_plural[-2:] == 'is':
        new_string = noun_to_plural[0:-2] + 'es'
        noun_to_plural = new_string

    elif noun_to_plural[-1] == 's':
        noun_to_plural += 'es'

    elif noun_to_plural[-1] == 'z':
        noun_to_plural += 'es'

    elif noun_to_plural[-1] == 'o':
        noun_to_plural += 'es'

    elif noun_to_plural[-1] == 'f':
        noun_to_plural += 'es'

    elif noun_to_plural[-2:] == 'oy':
        noun_to_plural += 's'

    elif noun_to_plural[-2:] == 'ch':
        noun_to_plural += 'es'

    elif noun_to_plural[-2:] == 'on':
        noun_to_plural += 'a'

    elif noun_to_plural[-2:] == 'um':
        noun_to_plural += 's'

    else:
        noun_to_plural += 's'

    print(noun_to_plural)

    end_program = input("end? [Y/N] ")



