# 1. Breadth-first search
def bfs(matrix, start):
    visited = [False] * len(matrix)
    queue = [start]
    order = []
    front = 0
    visited[start] = True

    while front < len(queue):
        current = queue[front]
        front += 1
        order.append(current)

        for neighbor in range(len(matrix)):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return order


# 2. Depth-first search
def dfs(matrix, start):
    visited = [False] * len(matrix)
    stack = [start]
    order = [start]
    next_column = [0] * len(matrix)
    visited[start] = True

    while stack:
        current = stack[-1]
        neighbor = next_column[current]

        if neighbor == len(matrix):
            stack.pop()
        else:
            # Remember where to continue when returning to this vertex.
            next_column[current] += 1
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                order.append(neighbor)

    return order


def main():
    try:
        n = int(input("Enter number of vertices: "))
        if n <= 0:
            print("Please enter a positive number of vertices.")
            return

        matrix = []
        print("Enter the adjacency matrix using 0 and 1 separated by spaces.")
        for i in range(n):
            row = [int(value) for value in input(f"Row {i}: ").split()]
            if len(row) != n or any(value not in (0, 1) for value in row):
                print(f"Each row must contain exactly {n} values (0 or 1).")
                return
            matrix.append(row)

        start = int(input(f"Enter starting vertex (0-{n - 1}): "))
    except (ValueError, EOFError):
        print("Please enter the required integer values.")
        return

    if not 0 <= start < n:
        print(f"Starting vertex must be between 0 and {n - 1}.")
        return

    print("BFS:", *bfs(matrix, start))
    print("DFS:", *dfs(matrix, start))


if __name__ == "__main__":
    main()
