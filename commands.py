#this contains basic commands that jarvis can perfom without the need of the ai model, such as opening applications, searching the web, etc. This is to reduce the number of calls to the ai model and make jarvis faster and more efficient.
import os
import json
import difflib
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
    
