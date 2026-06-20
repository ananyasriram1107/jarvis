#this contains basic commands that jarvis can perfom without the need of the ai model, such as opening applications, searching the web, etc. This is to reduce the number of calls to the ai model and make jarvis faster and more efficient.
import os
import json
import difflib
import webbrowser
from datetime import datetime
import requests
import psutil
import pyperclip


def find_app_shortcut(app_name):
    """Search the Windows Start Menu for a shortcut matching app_name.

    This function checks both the shared Start Menu and the current user's
    Start Menu Programs folder for .lnk files. It compares each shortcut
    filename (without the .lnk extension) to the requested name using
    difflib.get_close_matches() with a cutoff of 0.6. If a close match is
    found, the full shortcut path is returned immediately. If nothing matches,
    None is returned.
    """
    username = None
    try:
        username = os.getlogin()
    except OSError:
        username = os.environ.get("USERNAME") or os.environ.get("USER")

    start_menu_dirs = [
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
    ]

    if username:
        start_menu_dirs.append(
            os.path.join(
                r"C:\Users",
                username,
                r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs",
            )
        )

    app_name_lower = app_name.lower()

    for root_dir in start_menu_dirs:
        if not root_dir or not os.path.exists(root_dir):
            continue

        for root, _, files in os.walk(root_dir):
            for file_name in files:
                if not file_name.lower().endswith(".lnk"):
                    continue

                shortcut_name = os.path.splitext(file_name)[0]
                if difflib.get_close_matches(app_name_lower, [shortcut_name.lower()], n=1, cutoff=0.6):
                    return os.path.join(root, file_name)

    return None

store = {"chrome":r"C:\Users\Ananya\Desktop\google docs.lnk","google chrome":r"C:\Users\Ananya\Desktop\google docs.lnk","discord":r"C:\Users\Ananya\Desktop\Discord.lnk","spotify":r"C:\Users\Ananya\Desktop\Spotify.lnk"}

try:
    with open("apps.json", "r") as f:
        store = json.load(f)
except FileNotFoundError:
    pass  # use default store


def openapp(app_name):
    
    app_name = app_name.lower()
    if app_name in store:
        os.startfile(store[app_name])
        return f"Certainly, opening {app_name}..."
    else:
        match = difflib.get_close_matches(app_name, store.keys(), n=1, cutoff=0.6)
        if match:
            best_match = match[0]
            os.startfile(store[best_match])
            return f"Couldn't find '{app_name}', but opening {best_match}..."
        else:
            print( f"Sorry, I don't have {app_name} in my store.")
            link = input("Can you provide the path to the application you want to open? (or type 'no' to cancel): ")
            if link.lower() != 'no':
                if os.path.exists(link):
                    store[app_name] = link
                    os.startfile(link)
                    with open("apps.json", "w") as f:
                        json.dump(store, f)
                    return f"Certainly, opening {app_name}..."
                else:
                    return "The provided path does not exist. Please try again."
            else:
                return "Operation cancelled."
        
def closeapp(app_name):
    app_name = app_name.lower()
    if app_name in store:
        os.system(f"taskkill /f /im {app_name}.exe > nul 2>&1")
        return f"Certainly, closing {app_name}..."
    else:
        return f"Sorry, I don't have {app_name} in my store. Please open it first before trying to close it."
    
def websearch(query):
    import webbrowser
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching the web for '{query}'..."


def telltime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return f"The current time is {current_time}."

def telldate():
    from datetime import datetime
    now = datetime.now()
    current_date = now.strftime("%B %d, %Y")
    return f"Today's date is {current_date}."


    