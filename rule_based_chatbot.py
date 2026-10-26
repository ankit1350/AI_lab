def chatbot(user_input):
    if 'hello' in user_input or 'hi' in user_input:
        return "Hi, how are you."
    elif 'how are you' in user_input:
        return "I am fine, thanks for asking."
    elif 'your name' in user_input:
        return "I am a chatbot."
    elif 'bye' in user_input or 'exit' in user_input:
        return "Bye"
    else:
        return "I didn't understand that."
print("Welcome to the chatbot.")
print("Type 'Bye' or 'Exit' to Exit the chatbot.")
while True:
    user_input=input("Enter: ").lower().split()
    response=chatbot(user_input)
    print("Bot:" ,response)
    if 'bye' in user_input or 'exit' in user_input:
        break