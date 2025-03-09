import questionary
import os
import json
from yaml import safe_load

files = {}
namespace = ""
files_to_generate = []
namespace_folders_to_generate = []
minecraft_folders_to_generate = []
pack_mcmeta = {}
using_preset = bool

def load_options(file):
    with open(file, 'r') as file:
        content = file.read()
    options = safe_load(content)
    return options

def generate_pack():
    global namespace_folders_to_generate
    global minecraft_folders_to_generate

    #Generate pack.mcmeta for the user
    if "pack.mcmeta" in files_to_generate:
        global pack_mcmeta
        pack_mcmeta = {
            "pack": {
                "description": input("Enter the description for your pack.mcmeta file: "),
                "pack_format": int(input("Enter the current datapack format/version: "))
            }
        }

        with open("pack.mcmeta","w") as file:
            file.write(json.dumps(pack_mcmeta))

    #Generate tick.json and tick.mcfunction for the user
    if "tick.json / tick.mcfunction" in files_to_generate:
        tick_json = {"replace": False,"values": [namespace + ":tick"]}
        os.makedirs("data/minecraft/tags/function/", exist_ok = True)
        os.makedirs("data/" + namespace + "/function/", exist_ok = True)

        with open("data/minecraft/tags/function/tick.json","w") as file:
            file.write(json.dumps(tick_json))

        with open("data/" + namespace + "/function/tick.mcfunction","w") as file:
            file.write("")

    #Generate load.json and load.mcfunction for the user
    if "load.json / load.mcfunction" in files_to_generate:
        load_json = {"replace": False,"values": [namespace + ":tick"]}
        os.makedirs("data/minecraft/tags/function/", exist_ok = True)
        os.makedirs("data/" + namespace + "/function/", exist_ok = True)

        with open("data/minecraft/tags/function/load.json","w") as file:
            file.write(json.dumps(load_json))

        with open("data/" + namespace + "/function/load.mcfunction","w") as file:
            file.write("")

    #Generate all the user's requested namespace folders
    if "namespace folders" in files_to_generate:
        if not using_preset:
            namespace_folders_to_generate = questionary.checkbox("What folders should be generated in your namespace?", choices=files["folders"]).ask()

        for i in namespace_folders_to_generate:
            os.makedirs("data/" + namespace + "/" + i, exist_ok = True)

    if "minecraft folders" in files_to_generate:
        if not using_preset:
            minecraft_folders_to_generate = questionary.checkbox("What folders should be generated in the minecraft namespace?", choices=files["folders"]).ask()

        for i in minecraft_folders_to_generate:
            os.makedirs("data/minecraft/" + i, exist_ok = True)

def generate_preset():
    path = input("Enter the full path of the folder where your preset will be stored: ")
    name = input("Enter the name of your preset: ")
    preset = {"files_to_generate": files_to_generate, "namespace_folders_to_generate": namespace_folders_to_generate, "minecraft_folders_to_generate": minecraft_folders_to_generate}

    os.makedirs(path, exist_ok=True)
    with open(path + "/" + name + ".json", "w") as file:
        file.write(json.dumps(preset))

    print("Preset created successfully.")

def load_preset():
    global files_to_generate
    global namespace_folders_to_generate
    global minecraft_folders_to_generate

    path = input("Enter the full path to your preset.json file: ")

    with open(path, "r") as file:
        preset = json.load(file)
        files_to_generate = preset["files_to_generate"]
        namespace_folders_to_generate = preset["namespace_folders_to_generate"]
        minecraft_folders_to_generate = preset["namespace_folders_to_generate"]


def datapack_generator():
    global files
    global namespace
    global files_to_generate
    global using_preset
    files = load_options(__file__ + "\\..\\files.yaml")
    namespace = input("What is the namespace of your datapack? ")
    if questionary.select("Would you like to create from a preset or start from scratch?", choices = ["Use Preset","Start From Scratch"]).ask() == "Use Preset":
        using_preset = True
        load_preset()
    else:
        using_preset = False
        files_to_generate = questionary.checkbox("What would you like to generate?", choices=files["types"]).ask()

    generate_pack()

    if using_preset:
        print("Pack generated successfully.")
    else:
        if input("Pack generated successfully. Save as preset? (y/N): ") == "y":
            generate_preset()