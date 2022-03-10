from typing import List


def is_sorted(array: List[int]) -> bool:
    return all(array[i] >= array[i + 1] for i in range(len(array) - 1))