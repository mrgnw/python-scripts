# Flood fill implementation fo the code
# floodmap1.txt and floodmap2.txt


# Preliminary functions for making flood_fill implementation and testing easier
def map_string(map_list):
    if map_list == None:
        return "map_list is None"

    row = ""
    for i in map_list:
        for c in i:
            row += c
        #row += "\n"
    return row


# Generate a map, default size 20x20
def map_gen(w=20, h=20):
    map_row = [''] * w
    return [map_row] * h


def map(filename):
    rows = []
    with open(filename) as f:
        rows = f.readlines()
        w = len(rows[0])-1
        h = len(rows)

    return rows

#print map_string(map_gen(12,8))


# BASE: char == old_char
# work: char = new_char
# BASE: flood_fill (x+1, y+1) / (x-1, y-1) / (x+1, y-1) / (x-1, y+1)
def flood_fill(map, x = 0, y = 0, old =".", new = "*"):
    if x < 0 or x > len(map[0])-1:
        return
    if y < 0 or y > len(map)-1:
        return


    if not map[y][x] == old:
        return map# STOP - Base case

    # CHANGE THE STRING AT POSITION
    if map[y][x] == old:
        #print map[y]
        map[y] = map[y][:x] + new + map[y][x+1:]
        #print map_string(map)

        print map[y][x]

        flood_fill(map, x+1, y, old, new) # right
        flood_fill(map, x-1, y, old, new) # left
        flood_fill(map, x, y+1, old, new) # up
        flood_fill(map, x, y-1, old, new) # down


# Locate a char on the map
def find(map, char = '.'):
    y = -1
    x = -1
    for row in map:
        y += 1
        x = row.find(char)
        if x >= 0:
            return (x, y)

    return None

#BASE: Rooms are full
def count_rooms(map, char = '.'):
    rooms = 0 # I'm considering the hallway a room - Assuming

    while find(map, char) != None:
        x, y = find(map, char)
        #x = t[0]
        #y = t[1]

        flood_fill(map, x, y, char)
        rooms += 1
    else :
        return rooms

world = map('rooms.txt')
#print map_string(map())
#print map()

#print map_string(flood_fill(world, 5,5))
#world = map()

#print map_string(flood_fill(world, 8,1))
#world = map()
#
#print map_string(flood_fill(world, 8,0))

#print type(find(map()))
#
print ".\t", count_rooms(world)
print "2\t", count_rooms(world, '2')
print ".\t", count_rooms(world), "(world wasn't reset)"

world = map('rooms.txt')
print ".\t", count_rooms(world)

world = map('rooms.txt')
print "#\t", count_rooms(world, '#')

world = map('text_map.txt')
print "Text map:\t", count_rooms(world, '.')

