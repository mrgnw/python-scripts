from copy import deepcopy
import os.path



def read_map(fname):
    rows = []

    if os.path.exists(fname):
        with open(fname) as f:
            rows = f.readlines()

            w = len(rows[0])-1
            #print w

            h = len(rows)
            #print h
            #print rows
    else:
        # TODO: Generate a blank map when file does not exist
        print fname, 'does not exist'

        #for line in enumerate(map_gen()):
        #    rows[i] = line

    return rows


def map_string(map_list):
    if map_list == None:
        return "map_list is None"

    row = ""
    #print "* stringinate *"

    for i in map_list:
        for c in i:
            row += c
        #row += "\n"

    return row


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

        #print map[y][x]

        flood_fill(map, x+1, y, old, new) # right
        flood_fill(map, x-1, y, old, new) # left
        flood_fill(map, x, y+1, old, new) # up
        flood_fill(map, x, y-1, old, new) # down


class Map(object):

    def __init__(self, filename='mapfile1.txt'):
        self.rows  = read_map(filename)

    def __str__(self):
        return map_string(self.rows)

    def reset(self):
        pass

    def fill(self, x = 0, y = 0):
        return flood_fill(self.rows, x, y)

    def rotate(self):
        ''' rotates the map 90 degrees clockwise.
            Makes row 1 into column (last)
        '''
        pass

    #if __name__ == '__main__':
    #    single_room_map = Map("mapfile1.txt")
    #    multi_room_map = Map("mapfile2.txt")
    #    single_room_map.flood_fill(5,6)  # Prints the filled single-room map.
    #    single_room_map.flood_fill(3,2)  # Printed again from a different point.
    #    multi_room_map.flood_fill(5,6)
    #    multi_room_map.flood_fill(3,2)



treasure_map = Map('text_map.txt')
blank = Map('mapfile1.txt')

print
print treasure_map
#flood_fill(treasure_map.rows)
treasure_map.fill()
print treasure_map

treasure_map.fill(8,4)
print treasure_map
