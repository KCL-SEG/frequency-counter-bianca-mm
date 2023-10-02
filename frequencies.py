"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        if str(i) in frequencies.keys():
            frequencies[str(i)] += 1
        else:
            frequencies[str(i)] = 1
    return frequencies