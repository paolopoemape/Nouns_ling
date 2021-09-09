

#Start of the program.
#In case the user wants to end program, I started the input as N, which stands for
# "no", if the user changes to Y then the program will stop
end_program = "N"


while end_program != "Y":

#Statement to welcome the user
    noun_to_plural = input("Welcome to the plural convertor, enter your noun "
                           "to convert it to plural: ")

#If the last character of the input is 'x' then add 'es' to the noun
    if noun_to_plural[-1] == 'x':
        noun_to_plural += 'es'

#If the last character of the input is 'x' then add 'es' to the noun
    elif noun_to_plural[-2:] == 'is':
        new_string = noun_to_plural[0:-2] + 'es'
        noun_to_plural = new_string
#This elif will slice the string, check the last 2 strings on the string and the change it to plural
    elif noun_to_plural[-2:] == 'fe':
        new_string = noun_to_plural[0:-2] + 'ves'
        noun_to_plural = new_string

    elif noun_to_plural[-1] == 's' or noun_to_plural[-1] == 'z' or noun_to_plural[-1] == 'o'\
            or noun_to_plural[-1] == 'f':
        noun_to_plural += 'es'

    elif noun_to_plural[-2:] == 'oy':
        noun_to_plural += 's'

    elif noun_to_plural[-2:] == 'ch':
        noun_to_plural += 'es'
#elif statement to handle those nouns that have to characters that end on 'on' and then I replaced those characters with an 'a'
    elif noun_to_plural[-2:] == 'on':
        new_string = noun_to_plural[0:-2] + 'a'
        noun_to_plural = new_string

#elif statement that checks for irregular plurals using their two last characters (voqwl + y ) of the string.
    #then I added a 's' into the string.
    elif noun_to_plural[-2:] == 'ay' or noun_to_plural[-2:] == 'ey' or noun_to_plural[-2:] == 'iy' or \
            noun_to_plural[-2:] == 'oy' or noun_to_plural[-2:] == 'uy':
        noun_to_plural += 's'

    elif noun_to_plural[-2:] != 'ay' or noun_to_plural[-2:] != 'ey' or noun_to_plural[-2:] != 'iy' or \
            noun_to_plural[-2:] != 'oy' or noun_to_plural[-2:] != 'uy':
        new_string = noun_to_plural[0:-1] + 'ies'
        noun_to_plural = new_string
#elif statement to handle those nouns their two characters end with 'um', the program then adds a s at the end
    elif noun_to_plural[-2:] == 'um':
        noun_to_plural += 's'
#If the noun doesn't meet all the other requirmements then the convertor will
#add a 's' because that's usually the simple form.
    else:
        noun_to_plural += 's'

#Prints the noun converted to plurarl. I used it for testing purposes.
    print(noun_to_plural)
#Asks the user if they want to finish the program
    end_program = input("end? [Y/N] ")



