#!/usr/bin/python3
""" validUTF8 Validation Module """


def validUTF8(data):
    """
    Checks if data represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for num in data:
        if num & 0b11000000 == 0b10000000:
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            if num_bytes != 0:
                return False

            if num & 0b10000000 == 0:
                num_bytes = 0
            elif num & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif num & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif num & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

    return num_bytes == 0
