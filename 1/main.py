import mood_responses
while True:
    mood = input("How are you feeling today? ")
    if mood.lower() == "end":
        break
    mood_responses.mood_response(mood)