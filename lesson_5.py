import keyword
import string

user_input = input("Type a variable name: ")

new_string_filter = string.punctuation.replace ("_", "")

if  user_input[0].isdigit() :
    print (False)
elif not user_input.lower() == user_input:
    print (False)
elif user_input in keyword.kwlist:
    print (False)
elif "__" in user_input:
    print(False)
elif " " in user_input:
    print(False)
elif user_input:
    for element in user_input:
        if element  in new_string_filter:
           print(False)
           break
    print(True)
else:
     print(True)

