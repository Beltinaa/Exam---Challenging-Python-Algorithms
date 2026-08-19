def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    if not grid or not pattern:
        return []

    result = []

    directions = {
        "H": (0, 1),
        "H-": (0, -1),
        "V": (1, 0),
        "V-": (-1, 0),
        "D1": (1, 1),
        "D1-": (-1, -1),
        "D2": (1, -1),
        "D2-": (-1, 1)
    }

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for n, (dr, dc) in directions.items():

                if all(
                    0 <= r + i * dr < len(grid) and
                    0 <= c + i * dc < len(grid[0]) and
                    grid[r + i * dr][c + i * dc] == pattern[i]
                    for i in range(len(pattern))
                ):
                    result.append((r, c, n))

    return result

print(prism_detector(["XYZ", "ABC", "DEF"], "XBF"))
print(prism_detector(["ABC", "DEF", "GHI"], "ADG"))
print(prism_detector(["HELLO", "WORLD"], "LL"))