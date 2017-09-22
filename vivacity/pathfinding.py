from operator import itemgetter
from mapcreator import *

def string_to_map(text):
    text = text.strip('\n')
    return text.split('\n')

def set_start_on_map(_map, x, y):

    _map[y] = _map[y][:x] + 'S' + _map[y][x + 1:]

    return _map

def set_exit_on_map(_map, x, y):

    _map[y] = _map[y][:x] + 'E' + _map[y][x + 1:]

    return _map

def set_road_on_map(_map, cell_list):


    for cell in cell_list:
        _map[cell[1]] = _map[cell[1]][:cell[0]] + 'O' + _map[cell[1]][cell[0] + 1:]

    return _map

def is_wall(_map, x, y):
    if _map[y][x] == 'x':
        return True
    return False

def valid_surroundings(_map, x,y, counter, know_list = None):

    # get map length
    ymax = len(_map)
    xmax = len(_map[0])

    # get cells around where we are
    # none if they are after the walls
    left = (x-1, y, counter +1, ) if x-1 >= 0 else None
    right = (x+1 , y, counter+1,) if x+1 < xmax else None
    up = (x, y-1, counter+1,) if y-1 >= 0 else None
    down = (x, y+1, counter+1,) if y+1 < ymax else None

    #remove nones and remove walls
    possible_cells = [x for x in [left, right, up, down] if x is not None\
                      and not is_wall(_map, x[0], x[1])]
    #print("POSSIBLE CELLS {}".format(possible_cells))

    remove_cells = []
    for cell in possible_cells:
        for know_cell in know_list:
            if cell[0]==know_cell[0] and cell[1]==know_cell[1] \
                and cell[2] >= know_cell[2]:
                #print("REMOVE {}".format(cell))
                remove_cells.append(cell)

    for cell in remove_cells:
        possible_cells.remove(cell)

    return possible_cells

def transverse_path(start_x, start_y, know_path):

    path = sorted(know_path, key=itemgetter(2))[::-1]

    start_cell = [x for x in path if x[0]==start_x and x[1]==start_y][0]

    path.remove(start_cell)
    final_path = [start_cell]

    current_cell = start_cell
    for cell in path:
        if (cell[0]==current_cell[0] and current_cell[1]-1 <= cell[1] <=current_cell[1]+1 and cell[2]<current_cell[2]) or \
        (current_cell[0]-1 <= cell[0] <=current_cell[0]+1 and cell[1]==current_cell[1] and cell[2]<current_cell[2]):
            current_cell=cell
            final_path.append(cell)

    return final_path


def path_between_points(start_x, start_y, end_x, end_y, map_file_location):
    """ Given start and end coordinates and a map file,
            outputs the shortest path from start to end points on the map.

    Args:
        start_x (int): The x coordinate of the start position.
        start_y (int): The y coordinate of the start position.
        end_x (int): The x coordinate of the end position.
        end_y (int): The y coordinate of the end position.
        map_file_location (int): The file location of the map file to search through.

    Returns:
        The map with the path taken.
    """

    ## TODO improve this on map creator - should be 1 function
    with open(map_file_location, 'r') as f:
        map_lines = []
        for line in f.readlines():
            map_lines.append(line.strip())

    _map = map_lines


    ### Actual program starts here
    start = (start_x,start_y,)
    know_list = [(end_x,end_y,0,)]
    for x in know_list:
        possible = valid_surroundings(_map, x[0], x[1], x[2], know_list)
        know_list.extend(possible)

        flag_exit = False
        for cell in possible:
            if cell[0]==start[0] and cell[1]==start[1]:
                flag_exit = True
                break
        if flag_exit:
            break

    ## TODO Transverse path stored in known_list

    final_path = transverse_path(start_x, start_y, know_list)


    _map = set_road_on_map(_map, final_path)
    _map = set_start_on_map(_map, start_x, start_y)
    _map = set_exit_on_map(_map, end_x, end_y)

    ## print map as string
    map_output = map_to_str(_map)

    return map_output
