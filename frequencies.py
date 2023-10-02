"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        if i in frequencies.keys():
            frequencies[i] += 1
        else:
            frequencies[i] = 0
    return frequencies
