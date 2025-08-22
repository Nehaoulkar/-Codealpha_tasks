def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."


print(" Simple Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if user_message.lower().strip() == "bye":
        break

