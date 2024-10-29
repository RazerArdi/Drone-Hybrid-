import math

def normalize(value, min_val, max_val):
    """Normalize a value to be between 0 and 1 based on min and max values."""
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def calculate_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def clip_value(value, min_val, max_val):
    """Limit the value to be within the specified min and max range."""
    return max(min(value, max_val), min_val)

