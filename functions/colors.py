from collections import defaultdict
import math


# Functions included in this file:
# # generate_label_colors
# # labels_to_colors


def generate_label_colors(labels: list, colors: list, palette='Set2'):
    """Matches labels with colors
    If there are more labels than colors, repeat and cycle through colors
    """
    label_colors = defaultdict(dict)
    num_repeats = math.ceil(len(labels) / len(colors))
    for label in enumerate(labels):
        label_colors[label[1]] = (colors * num_repeats)[label[0]]
    return {**label_colors}
