print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("🤖 Chatbot: Goodbye!")
        break

    elif "hello" in user or "hi" in user:
        print("🤖 Chatbot: Hi there!")

    elif "how are you" in user:
        print("🤖 Chatbot: I am doing great!")

    elif "your name" in user:
        print("🤖 Chatbot: I am CodSoft Bot")

    elif "help" in user:
        print("🤖 Chatbot: I can answer basic questions!")

    elif "time" in user:
        import datetime
        print("🤖 Chatbot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))

    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")