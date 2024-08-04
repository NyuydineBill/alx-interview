#!/usr/bin/python3
"""Solution to Lockboxes problem"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Parameters:
    boxes (list of lists): A list where each element is a list containing keys to other boxes.
    
    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    for k in range(1, len(boxes)):
        unlocked = False
        for i in range(len(boxes)):
            if k in boxes[i] and k != i:
                unlocked = True
                break
        if not unlocked:
            return False

    return True
