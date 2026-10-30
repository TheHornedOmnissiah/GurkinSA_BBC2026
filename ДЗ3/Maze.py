from random import *


def create_maze(n, m):
    room_types = ["E", "C", "M", "T", "P", "K"]
    room_chance = [5, 3, 2, 2, 0, 0]
    player_map = [['#' for i in range(m)] for _ in range(n)]
    real_map = [choices(room_types, weights=room_chance, k=m) for _ in range(n)]
    px = randint(0, m - 1)
    py = randint(0, n - 1)
    kx = randint(0, m - 1)
    ky = randint(0, n - 1)
    real_map[py][px] = "P"
    real_map[ky][kx] = "K"
    return real_map, player_map


monster_type = [["Beholder", 100, 20], ["Skeleton", 20, 7], ["Rat-thing", 15, 15]]
monster_chance = [1, 4, 3]
chest_item = ["map", "sword", "enchanting shard", "hp potion", "steel chestplate", ["Mimic", 30, 10]]
items = [{"name": "map", "usage": ["Use", "Throw"], "desc": "let you see your location"},
         {"name": "sword", "usage": ["Throw"], "desc": "Do +15 dmg, don't stack"},
         {"name": "enchanting shard", "usage": ["Use", "Throw"], "desc": "let you chant items"},
         {"name": "hp potion", "usage": ["Use", "Throw"], "desc": "Heals 25 hp"},
         {"name": "steel chestplate", "usage": ["Throw"], "desc": "reduse taken dmg by 5, dont stack"}]
inventory = []
hp = 100
maxhp = 100
position = [0, 0]
escaped = False

x = int(input("Enter dungeons length: "))
y = int(input("Enter dungeons width: "))
r_map, p_map = create_maze(y, x)

while not escaped and hp > 0:
    p_map[position[0]][position[1]] = "@"
    if r_map[position[0]][position[1]] == "E":
        print(" ".join(i) for i in p_map)
        action = input(f"hp:{hp}/{maxhp}, what to do: w - go up, a - go left, s - go down, d -go right, i - see inventory, q - quit")
        if action == "w":
            if position[1] - 1 < 0:
                print("You bumped into wall, you took 5 damdge, ouch!")
                hp -= 5
            else:
                p_map[position[0]][position[1]] = r_map[position[0]][position[1]]
                position[1] -= 1
        elif action == "s":
            if position[1] + 1 == y:
                print("You bumped into wall, you took 5 damdge, ouch!")
                hp -= 5
            else:
                p_map[position[0]][position[1]] = r_map[position[0]][position[1]]
                position[1] -= 1
        elif action == "a":
            if position[0] - 1 < 0:
                print("You bumped into wall, you took 5 damdge, ouch!")
                hp -= 5
            else:
                p_map[position[0]][position[1]] = r_map[position[0]][position[1]]
                position[1] -= 1
        elif action == "d":
            if position[0] - 1 == x:
                print("You bumped into wall, you took 5 damdge, ouch!")
                hp -= 5
            else:
                p_map[position[0]][position[1]] = r_map[position[0]][position[1]]
                position[1] -= 1
        elif action == "i":
            print(*inventory)
            itm = input("Choose item: ")
            if itm not in inventory:
                print("You don't have this")
                


