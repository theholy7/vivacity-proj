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

    collision_output = 'this-is-the-string-that-your-code-will-output'

    return collision_output