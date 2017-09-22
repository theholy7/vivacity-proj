from operator import itemgetter

from hashiterator import *
from mapcreator import *
from pathfinding import *

# USE this function to check for candidate cells when investigating the next
# step in a path


def candidate_cells(start_x, start_y, know_path):

    path = sorted(know_path, key=itemgetter(2))[::-1]

    start_cell = [x for x in path if x[0] == start_x and x[1] == start_y][0]

    path.remove(start_cell)
    final_path = [start_cell]
    current_cell = start_cell

    candidate_cells = [cell for cell in path if
                       (cell[0] == current_cell[0] and
                        current_cell[1] - 1 <= cell[1] <= current_cell[1] + 1 and
                        cell[2] < current_cell[2])
                       or
                       (current_cell[0] - 1 <= cell[0] <= current_cell[0] + 1
                        and cell[1] == current_cell[1]
                        and cell[2] < current_cell[2])]

    return candidate_cells


# TODO Adapt this function to score each path
def score_maps(start_x, start_y, all_paths):

    path = sorted(all_paths, key=itemgetter(2))[::-1]
    current_cell = [x for x in path if x[0] == start_x and x[1] == start_y][0]

    total = 2
    c = candidate_cells(current_cell[0], current_cell[1], path)
    best_score_path = [current_cell]
    while len(c) != 0:

        if len(c) == 1:
            current_cell = c[0]
            total += c[0][0] + c[0][1]
            best_score_path.append(current_cell)

        if len(c) > 1:
            temp = {}
            for i, n in enumerate(c):
                temp[total + n[0] + n[1]] = n

            best = min(temp.keys())
            current_cell = temp[best]
            best_score_path.append(current_cell)

        c = candidate_cells(current_cell[0], current_cell[1], path)

    return best_score_path


def all_together(start_x, start_y, end_x, end_y, coordinates_directory, number_of_zeros):
    """ Takes the files in the coordinates directory and creates a map. Then
            given start and end coordinates it outputs the shortest path from the start
            to end points on the map. This map is then saved to a file location.
            The function will then take the string of the path taken,
            find the hash collisions with the number of zeros input and
            return the hash result.

    Args:
        start_x (int): The x coordinate of the start position.
        start_y (int): The y coordinate of the start position.
        end_x (int): The x coordinate of the end position.
        end_y (int): The y coordinate of the end position.
        coordinates_directory (string): Directory containing the files to parse.
        number_of_zeros (int): The number of zeros to be searching for at the start of the hash.

    Returns:
        The collisions string the function has built.
    """

    string_map = parse_and_create_map(coordinates_directory)
    _map = string_to_map(string_map)

    all_paths = get_all_paths(start_x, start_y, end_x, end_y, _map)

    best_score_path = score_maps(start_x, start_y, all_paths)

    input_hash = ""
    for x, y, s in best_score_path:
        input_hash += "{}{}".format(x if x > 9 else "0{}".format(x),
                                    y if y > 9 else "0{}".format(y))

    result = find_zero_collision_from_salt(salt=input_hash, number_of_zeros=number_of_zeros)

    _map = set_road_on_map(_map, best_score_path)
    _map = set_start_on_map(_map, start_x, start_y)
    _map = set_exit_on_map(_map, end_x, end_y)

    with open(result, 'w') as f:
        f.write(map_to_str(_map))

    collision_output = result

    return collision_output
