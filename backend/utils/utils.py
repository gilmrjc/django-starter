"""
Utils functions.
"""
import random
import string


def random_string_generator(size=6, chars=string.ascii_lowercase):
    """
    Generate a random string.
    """
    while True:
        yield "".join(random.choice(chars) for _ in range(size))
