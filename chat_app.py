# chat_app.py
def chat():
    print("Welcome to the simple Chat App!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Bye! Have a great day.")
            break
        elif "hello" in user_input.lower():
            print("Bot: Hi there!")
        elif "how are you" in user_input.lower():
            print("Bot: I'm a bot, always good!")
        else:
            print("Bot: Sorry, I don't understand.")

chat()