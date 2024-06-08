def mood_response(mood):
    try:
        if mood.lower() == "happy":
            print("That's amazing!!")
        elif mood.lower() == "sad":
            print("I hope you feel better!") 
        elif mood.lower() == "excited":
             excite = input("What are you excited about? ")
             print("Wow!! That's great!")
        elif mood.isdigit():
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("Error. Bad input")
    except Exception:
         print("Error.")
    