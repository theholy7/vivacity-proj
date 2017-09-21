import glob
import re


def get_filelist(path):
    if '/' != path[-1]:
        path += '/'
    return glob.glob(path + '*.txt')


def parse_file(path):
    coordinates = []

    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip().strip(',')
            coordinates.extend(line.split(','))

    return coordinates


def parse_coordinates(coord_string):
    rg = re.compile(r'(?P<x>(?<=x)\d+).(?P<y>(?<=y)\d+)')
    match = re.search(rg, coord_string)

    return (int(match.group('x')), int(match.group('y')))


def create_map(x, y):
    horizontal = "." * x
    created_map = [horizontal] * y
    return created_map


def set_cross_on_map(_map, x, y):

    _map[y] = _map[y][:x] + 'x' + _map[y][x + 1:]

    return _map


def map_to_str(_map):
    return "\n".join(_map) + '\n'


def parse_and_create_map(coordinates_directory):
    """Parses files in the input directory into a map
        then saves this to a file location and returns it.

    Args:
        coordinates_directory (string): Directory containing
                the files to parse.

    Returns:
        The created map.
    """
    filelist = get_filelist(coordinates_directory)

    total_coordinates = []
    for filename in filelist:
        file_coord = parse_file(filename)
        total_coordinates += file_coord

    clean_coord = []
    xmax = 0
    ymax = 0
    for xy in total_coordinates:
        x, y = parse_coordinates(xy)
        if x >= xmax:
            xmax = x + 1
        if y >= ymax:
            ymax = y + 1

        clean_coord.append((x, y,))

    _map = create_map(xmax, ymax)

    for x, y in clean_coord:
        _map = set_cross_on_map(_map, x, y)

    return map_to_str(_map)
