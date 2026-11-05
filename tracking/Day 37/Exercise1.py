def calculate_area(width, height):
    if width <= 0:
        raise ValueError("Dimensions must be positive")
    if height <= 0:
        raise ValueError("Dimensions must be positive")
    area = width * height
    return area

print(calculate_area(2, 0))