import hashlib
import logging

logger = logging.getLogger(__name__)

def md5_string(word):
    return hashlib.md5(("{}".format(word)).encode('utf-8')).hexdigest()

def correct_n_zeros_in_md5_hash(md5_hash, n):
    if n > len(md5_hash):
        raise ValueError("n bigger than hash")

    sliced_hash = md5_hash[:n]
    for c in sliced_hash:
        if not c.isdigit():
            return False
        if int(c) != 0:
            return False

    return True

def number_after_zeros_in_md5_hash(md5_hash, n):
    if n > len(md5_hash):
        raise ValueError("n bigger than hash")

    sliced_hash = md5_hash[n:n+1]
    if sliced_hash[0].isdigit():
        c = int(sliced_hash[0])
        return True, c

    return False, None

def get_position(i):
    return i % 32



def find_zero_collision_from_salt(salt, number_of_zeros):
    """Finds the hash collisions string returns it.

    Args:
        salt (string): The salt to iterate and hash.
        number_of_zeros (int): The number of zeros to be searching for at the start of the hash.

    Returns:
        The collisions string the function has built.
    """
    # renaming
    start = salt
    num = number_of_zeros


    password = ["-"]*10
    pass_set = set(password)
    position_set = set()

    password_not_found = True
    num_trial = 1

    while password_not_found:
        test_string = "{start}{num}".format(start=start, num=num_trial)

        test_hash = md5_string(test_string)

        if not correct_n_zeros_in_md5_hash(test_hash, num):
            num_trial += 1
            continue

        # put char at this position
        is_number, number = number_after_zeros_in_md5_hash(test_hash, num)

        if is_number and number not in position_set:
            position_set.add(number)

            position_to_get_number = get_position(num_trial)

            collected_char = test_hash[position_to_get_number]


            password[number] = collected_char
            pass_set = set(password)
            logger.info(collected_char)

            if '-' not in pass_set:
                password_not_found = False

        num_trial += 1


    collision_output = "".join(password)

    with open("output_{}_{}".format(salt, number_of_zeros), 'w') as f:
        f.write(collision_output)

    return collision_output
