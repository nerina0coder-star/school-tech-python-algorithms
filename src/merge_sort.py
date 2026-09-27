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


    while not any(i == 0 for i in [len(right), len(left)]):
        if left[0] < right[0]:  # type: ignore[operator]
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))

    if len(right) > 0:
        out.extend(right)

    if len(left) > 0:
        out.extend(left)


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

sorting = [0, 99, 87, 53, 828, 973, 7, 99, 34]

print(f"Executing merge_sort({sorting})...")
print(merge_sort(sorting))

