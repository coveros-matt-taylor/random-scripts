from modules.functions import *

inp = input(">")
print(parse(inp))

room2 = Scene(dirs={"north": None}, blurb=["Welcome to the second room"])
entrance = Scene(dirs={"north": room2}, nouns={"door"}, blurb=["Line one", "Line two"])

run_room(entrance)
