from kivy.app import App
import json
with open("teste.json", "r") as f:
    g = json.load(f)

    print(str(g))