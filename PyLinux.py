print("PyLinux 4.0 - Temporary Shell")
print("Type 'help' for help")
f = False
while not f:
    g = input("#:")
    if g == "setup":
        f = True
    elif g == "help":
        print("Type 'setup' to start")
    else:
        print(f"'{g}' is not recognised as a command")
print("Importing Base System Requirements")
try:
    from pathlib import Path
    import requests
    import time
    import random
    from tqdm import tqdm
    import runpy
    from urllib.parse import quote
    import shutil
    import os
except Exception as e:
    print(f"Error {e}. SOMETHING BAD HAPPENED. SOME COMMANDS MAY FAIL")
    if input("CONTINUE ANYWAYS? (Y/N) ").strip().lower() == "n":
        exit()
time.sleep(1.2)
print("Done")
time.sleep(0.1)
print("Defining Functions")
def write():
    location = input("ENTER PATH: ")
    content = input("ENTER TEXT: ")
    Path(location).write_text(content)
    print("Done")
def read():
    location = input("ENTER PATH: ")
    print(Path(location).read_text())
def mkdir():
    location = input("ENTER PATH: ")
    Path(location).mkdir(exist_ok=True)
    print("Done")
def execute():
    location = input("ENTER PATH: ")
    runpy.run_path(str(location))
def request():
    url = input("ENTER URL: ")
    d = requests.get(url, timeout=5)
    data = d.text
    if input("SAVE DATA (Y/N): ").strip().lower() == "y":
        path = input("PATH: ")
        Path(path).write_text(data)
        print("Done")
    else:
        print(data)
def cd():
    global Sandbox
    path = input("ENTER PATH: ")
    if path.startswith("/") or path.startswith("\\") or path.startswith("..") and Sandbox:
        print("Use cd with no path to go up one level")
        return
    if path != "":
        os.chdir(path)
    else:
        os.chdir("..")
        if os.path.basename(os.getcwd()) != "system" and Sandbox:
            os.chdir("system")
    print("Done")
def browser():
    text = input("ENTER TEXT: ")
    data = requests.get(f"https://api.duckduckgo.com/?q={quote(text)}&format=json")
    success = False
    pbar = tqdm(range(random.randint(20,70)),desc="Loading Browser",unit="")
    for i in pbar:
        if i >= random.randint(10,40):
            pbar.set_description("Downloading Results")
        if i >= random.randint(41,50):
            pbar.set_description("Phrasing Results")
        if i >= random.randint(51,60):
            pbar.set_description("Formatting Results")
        if i >= 61:
            pbar.set_description("Finishing Off")
        time.sleep(0.05)
    if data.json()["Heading"] != "":
        print(f"============= {data.json()['Heading']} ==============")
        success = True
    if data.json()["AbstractText"] != "":
        success = True
        print("Summary:")
        print(data.json()["AbstractText"])
        print("====================")
    for i in data.json().get("Results"):
        success = True
        if "Text" in i:
            print(i["Text"])
            print(i["FirstURL"])
            print("____________________")
    if data.json()["RelatedTopics"]:
        success = True
        print("========== Related Topics ==========")
    for i in data.json().get("RelatedTopics"):
        if "Text" in i:
            print(i["Text"])
            print("____________________")
    if not success:
        print(f"No Results For '{text}'")
    print("")
    print("Done")
def shutdown():
    if input("ARE YOU SURE YOU WANT TO DO THIS? (Y/N) ").strip().lower() == "y":
        if os.path.basename(os.getcwd()) == "system":
            time.sleep(0.8)
            print("GOODBYE")
            time.sleep(1.5)
            os.chdir("..")
            shutil.rmtree("system")
            print("SYSTEM DELETED. EXITING ENVIROMENT")
            exit()
        elif not Sandbox:
            time.sleep(0.1)
            print("GOODBYE")
            time.sleep(0.8)
            exit()
        print("Run this in the 'system' directory")
def exitSandbox():
    global Sandbox
    if input("ARE YOU SURE YOU WANT TO DO THIS? (Y/N) ").strip().lower() == "y":
        if not Sandbox:
            print("Sandbox is already exited")
            return
        if os.path.basename(os.getcwd()) == "system":
            time.sleep(0.8)
            print("GOOD LUCK")
            time.sleep(1.5)
            os.chdir("..")
            shutil.rmtree("system")
            print("SYSTEM DELETED. HAVE FUN!")
            Sandbox = False
        else:
            print("Run this in the 'system' directory")
def joke():
    d = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt", timeout = 5)
    data = d.text
    print(data)
def ls():
    print(os.listdir("."))
def pkg():
    if input("INSTALL PACKAGE? (Y/N): ").lower().strip() == "y":
        name = input("PACKAGE NAME: ")
        if input("INSTALL LOCAL? (Y/N)").strip().lower() == "n":
            url = input("PACKAGE URL: ")
            package_data = requests.get(url).text
            cmd[name] = lambda data=package_data: exec(data,{"__name__":"__main__"})
        else:
            path = input("ENTER PATH: ")
            cmd[name] = lambda data=Path(path).read_text(): exec(data,{"__name__":"__main__"})
        pbar = tqdm(range(random.randint(50,150)),desc="Installing Package",unit="")
        for i in pbar:
            if i >= random.randint(10,30):
                pbar.set_description("Extracting Files")
            if i >= random.randint(31,70):
                pbar.set_description("Setting up Package")
            if i >= random.randint(71,100):
                pbar.set_description("Installing Dependancies")
            if i >= random.randint(101,130):
                pbar.set_description("Finishing Up")
            if i >= 131:
                pbar.set_description("Optimising Package")
            time.sleep(0.05)
        print("Done")
            
def spam():
    for i in range(random.randint(50,75)):
        print(i*random.randint(2,7))
        time.sleep(0.1)
    print("Done")
def whereami():
    print(os.getcwd())
def rm():
    path = input("ENTER PATH: ")
    Path(path).unlink()
    print("Done")
def rmdir():
    path = input("ENTER PATH: ")
    Path(path).rmdir()
    print("Done")
def e():
    print("""
    write: writes files
    read: reads files
    joke: tells a joke.
    execute: executes a file
    browser: browse DA INTERNET (no visiting websites)
    mkdir: creates a directory
    request: makes a request to DA INTERNET
    ls: lists stuff. i think
    help: helps (allegedly)
    whereami: tells you your location (not in real life)
    cd: enters a directory
    rm: deletes files
    pkg: install stuff. run them by calling the package name
    rmdir: deletes directories
    exit: Erases the OS
    exitSandbox: Leave the sandbox. Embrace the real world.
    """)
print("Done")
time.sleep(0.5)
print("Creating System Directory")
time.sleep(0.7)
Path("system").mkdir(exist_ok=True)
print("Done")
print("Creating Variables")
cmd = {
    "write":write,
    "read":read,
    "execute":execute,
    "request":request,
    "joke":joke,
    "help":e,
    "cd":cd,
    "ls":ls,
    "SPAM":spam,
    "whereami":whereami,
    "rm":rm,
    "rmdir":rmdir,
    "browser":browser,
    "exit":shutdown,
    "exitSandbox": exitSandbox,
    "pkg":pkg,
    "mkdir":mkdir
}
Sandbox = True
time.sleep(0.6)
print("Done")
time.sleep(0.5)
print("Starting Enviroment")
print("Type 'help' for help. Do NOT create any folders called 'system' unless you want a bad time")
time.sleep(1)
print("Also don't try and break this thing to 'escape the sandbox'. There's a command for that. Break it for fun!")
os.chdir("system")
for i in tqdm(range(100), desc="Booting",unit=""):
    time.sleep(0.01)
while 1 == 1:
    c = input("#:")
    if c in cmd:
        try:
            cmd[c]()
        except Exception as e:
            print(f"ERROR: {e}")
    else:
        print(f"'{c}' is not a recognised command.")
