import config
from assistant import handle_input
from voice import speak, voice_input
# This is the main file that will run the assistant.
# It will be responsible for taking user input and passing it to the assistant.py file for processing.

def main():
    print(f"Hello {config.USER_NAME}, I am {config.ASSIST_NAME}. What are we doing today?")
    speak(f"Hello {config.USER_NAME}, I am {config.ASSIST_NAME}. What are we doing today?")
    while True:
        user_input = voice_input()
        if user_input is None:
            user_input = input("You: ")
        else:
            print(f"You said: {user_input}")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"{config.ASSIST_NAME}: Goodbye {config.USER_NAME}! Have a great day!")
            speak(f"Goodbye {config.USER_NAME}! Have a great day!")
            break
        else:
            response = handle_input(user_input)
            print(f"{config.ASSIST_NAME}: {response}")
            speak(response)
            
if __name__ == "__main__":
    main()