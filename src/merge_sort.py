from __future__ import annotations
from math import floor
from typing import TypeVar, TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed import SupportsRichComparison
    T = TypeVar("T", bound=SupportsRichComparison)

def merge(
    left: list[SupportsRichComparison],
    right: list[SupportsRichComparison],
    /
) -> list[SupportsRichComparison]:

    out: list[SupportsRichComparison] = []

    left_index = 0
    right_index = 0

    print(f"Index {left_index} for list (left) {left}")
    print(f"Index {right_index} for list (right) {right}")


    while all(
            len(side) - 1 >= index
            for side, index in
            [(left, left_index), (right, right_index)]
    ):
        if left[left_index] < right[right_index]:  # type: ignore[operator]
            out.append(left[left_index])
            left_index += 1
        else:
            out.append(right[right_index])
            right_index += 1
        print(f"Index {left_index} for list (left) {left}")
        print(f"Index {right_index} for list (right) {right}")

    if len(right) > right_index:
        out.extend(right[right_index:])

    if len(left) > left_index:
        out.extend(left[left_index:])

    print(f"Out: {out}")
    print("-" * 10)


    return out


def merge_sort(sorting: list[T], /) -> list[T]:

    if len(sorting) == 1:
        return sorting

    middle = floor(len(sorting) / 2)

    left = sorting[0:middle]
    right = sorting[middle:]

    return merge(
        merge_sort(left), merge_sort(right)  # type: ignore[arg-type]
    )  # type: ignore[return-value]

if __name__ == "__main__":
    sorting = [0, 99, 87, 53, 828, 973, 7, 99, 34]

    print(f"Executing merge_sort({sorting})...")
    print(merge_sort(sorting))

