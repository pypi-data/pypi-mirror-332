import questionary
import os
import json
from yaml import safe_load

files = {}
namespace = ""
files_to_generate = []
pack_mcmeta = {}

def load_options(file):
    with open(file, 'r') as file:
        content = file.read()
    options = safe_load(content)
    return options

def generate_pack():
    #Generate pack.mcmeta for the user
    if "pack.mcmeta" in files_to_generate:
        pack_mcmeta["pack"]["description"] = input("Enter the description for your pack.mcmeta file: ")
        pack_mcmeta["pack"]["pack_format"] = int(input("Enter the current datapack format/version: "))

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
        folders_to_generate = questionary.checkbox("What folders should be generated in your namespace?", choices=files["folders"]).ask()

        for i in folders_to_generate:
            os.makedirs("data/" + namespace + "/" + i, exist_ok = True)

    if "minecraft folders" in files_to_generate:
        folders_to_generate = questionary.checkbox("What folders should be generated in the minecraft namespace?", choices=files["folders"]).ask()

        for i in folders_to_generate:
            os.makedirs("data/minecraft/" + i, exist_ok = True)

def datapack_generator():
    global files
    global namespace
    global files_to_generate
    files = load_options(__file__ + "\\..\\files.yaml")
    namespace = input("What is the namespace of your datapack? ")
    files_to_generate = questionary.checkbox("What would you like to generate?", choices=files["types"]).ask()

    generate_pack()