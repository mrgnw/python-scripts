# Program for playing the game of Life.
from life import LifeGrid

# Define the initial configuration of live cells. 
INIT_CONFIG = [ (1,1), (1,2), (2,2), (3,2), (3,1), (2,3), (3,4), (2,4), (3, 3) ]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8


def main(): 
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game.
    print draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        print draw(grid)


# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    live_cells = list()
  
    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):
            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)
            #print neighbors
     
            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or \
                (neighbors == 3):
                live_cells.append((i, j))
  
    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells)


# Prints a text-based representation of the game grid.
def draw(grid):
    grid_map = ''
    for r in range(grid.num_rows()):
        for c in range(grid.num_cols()):
            if grid.is_live_cell(r,c):
                grid_map += str(grid.num_live_neighbors(r,c)) + ' '
            else:
                grid_map += ". "
        grid_map += '\n'
    return grid_map

# Executes the main routine.  
main()
