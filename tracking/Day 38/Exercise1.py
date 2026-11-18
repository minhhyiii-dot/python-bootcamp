def get_average(score):
    total = sum(score)
    if len(score) == 0:
        raise ValueError("Score cannot be empty")
    return total / len(score)

def show_result(score):
    avg = get_average(score)
    return f"Average: {avg}"


print(show_result([1, 4, 5, 2]))