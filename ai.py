def get_response(user_input):
    # Define some predefined patterns and corresponding responses
    patterns = ['hello', 'how are you', 'bye']
    responses = ['Hello!', 'I am fine, thank you!', 'Goodbye!']

    # Check if the user input matches any pattern
    for pattern, response in zip(patterns, responses):
        if pattern in user_input.lower():
            return response

    # If no pattern matches, return a default response
    return "Sorry, I don't understand."

# Main loop for AI interaction
while True:
    user_input = input("User: ")
    ai_response = get_response(user_input)
    print("AI: " + ai_response)
    if user_input.lower() == 'bye':
        break
