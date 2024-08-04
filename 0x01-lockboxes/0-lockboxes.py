#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each element is a list containing keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Boolean list to track which boxes are unlocked
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the first box's keys
    
    while keys:
        current_key = keys.pop()  # Get the next key to use
        for key in boxes[current_key]:  # Iterate over all keys in the current box
            if key < n and not unlocked[key]:  # Check if the key is valid and the box is not yet unlocked
                unlocked[key] = True  # Mark the box as unlocked
                keys.append(key)  # Add the key to the list of keys to use
    
    return all(unlocked)  # Check if all boxes have been unlocked
