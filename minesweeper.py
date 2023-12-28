import random

def print_map(map, total_tiles, width):
    for i in range(0, total_tiles):
        print(map[i], end = " ")

        if ((i+1) % width) == 0:
            print("")


def map_maker():
    ## width dimensions
    dim_width = int(input("Please enter the width of your board: "))
    if dim_width < 8:
        print("Sorry, the width must be greater than or equal to 8")
        dim_width = int(input("Please enter the width of your board: "))


    ## height dimensions
    dim_height = int(input("Please enter the height of your board: "))
    if dim_height < 1:
        print("Sorry, the height must be positive")
        dim_height = int(input("Please enter the height of your board: "))


    ## total tiles and ghosts
    total_tiles = dim_height * dim_width
    total_ghosts = random.randint(1,total_tiles)
    random_ghost_pos = random.sample(range(0, total_tiles), total_ghosts)
    random_ghost_pos.sort()
    index_ghost_pos = 0

    ## player_map and ghost_map
    player_map = []
    ghost_map = []


    ## initializing player and ghost map
    for i in range(0, total_tiles):
        player_map.append("_")

        if (index_ghost_pos < total_ghosts) and (i == random_ghost_pos[index_ghost_pos]):
            ghost_map.append("G")
            index_ghost_pos += 1
        else:
            ghost_map.append("_")

    print_map(ghost_map, total_tiles, dim_width)
    print("")
    print_map(player_map, total_tiles, dim_width)
    
map_maker()