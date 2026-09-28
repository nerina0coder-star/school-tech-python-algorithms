


def dfs(current: int, mapped: dict[int, list[int]], /, *, _searched: list[int] | None = None) -> None:
    if _searched is None:
        _searched = []
    _searched.append(current)

    print(f"Searched cord: {current}")

    for cord in mapped[current]:
        if cord in _searched:
            continue
        dfs(cord, mapped, _searched=_searched)


if __name__ == "__main__":
    searching = {
        0: [1, 5],
        1: [2, 6],
        2: [3, 7],
        3: [4, 8],
        4: [5, 9],
        5: [6, 10],
        6: [4],
        7: [3],
        8: [2],
        9: [1],
        10: [0]
    }

    print(f"Doing DFS {searching}")

    dfs(0, searching)

