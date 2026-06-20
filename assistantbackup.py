from commands import openapp, closeapp
from ai_client import askai
import string
#this file will be responsible for processing the user input and determining whether to call a command
#from commands.py or to send the input to the ai model using askai from ai_client.py.
#It will also be responsible for maintaining the conversation history and context for the ai model.


last_opened_app = None

def normalize_input(user_input):
    for char in user_input:
        if char in string.punctuation:
            user_input = user_input.replace(char, '')
    user_input = user_input.strip()
    return user_input.lower()

def get_intent(user_input):
    user_input = normalize_input(user_input)
    open_commands = ["open", "launch", "start"]
    close_commands = ["close", "exit", "terminate"]

    for command in open_commands:
        if command in user_input:
            return "open"

    for command in close_commands:
        if command in user_input:
            return "close"

    return "askai"

def get_target(user_input, intent):
    filler = ["the", "a", "an", "my", "please", 
           "hey", "jarvis", "can", "you", "could", "would", "for", "me", "i", "want", 
           "to", "like", "need", "help", "with", "and", "of","little","shit","piece","of","asshole","dipshit"
           "would", "for", "me", "i", "want", "to", "like", "need", "help", "with", "and", "of",
           "on", "in", "at", "by", "from", "is", "are", "was", "were", "be", "been", "being","you","can","could","would","should","may","might","must","shall","will"]
    words = user_input.split()
    words = [word for word in words if word not in filler]
    user_input = " ".join(words)
    user_input = user_input.strip()
    
    keywords = ["open", "launch", "start", "close", "exit", "terminate"]
    for keyword in keywords:
        if keyword in words:
            idx = words.index(keyword)
            return " ".join(words[idx+1:])

    return user_input  # fallback for ASK_AI



def handle_input(user_input):
    global last_opened_app
    user_input = normalize_input(user_input)
    intent = get_intent(user_input)
    pronouns = ["it", "that", "this"]
    words = user_input.split()
    if intent == "close" and any(word in pronouns for word in words):
        if last_opened_app:
            app = last_opened_app
            last_opened_app = None
            return closeapp(app)
    target = get_target(user_input, intent)
   
    if intent == "open":
        response = openapp(target)
        if "opening" in response:
            # extract actual app name from response
            last_opened_app = response.split("opening ")[-1].replace("...", "")
            return response
    elif(intent == "close"):
        return closeapp(target)
    else:
        return askai(user_input)