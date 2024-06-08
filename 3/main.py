import text_utils
while True:
    s = input("Enter a string to  manipulate:\n >> ")
    if s.lower() == "end":
        break
    text_utils.reverse_string(s)
    text_utils.capitalize_string(s)
    text_utils.lowercase_string(s)
    
