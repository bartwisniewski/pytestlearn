
from typing import List


def quicksort_step(unsorted_list: List[float], start, end) -> None:
    if start >= end:
        return

    pivot: int = int((start+end) / 2)
    pivot_value = unsorted_list[pivot]

    unsorted_list[end], unsorted_list[pivot] = unsorted_list[pivot], unsorted_list[end]
    position = start
    for i in range(start, end):
        if unsorted_list[i] < pivot_value:
            unsorted_list[i], unsorted_list[position] = unsorted_list[position], unsorted_list[i]
            position += 1
    unsorted_list[end], unsorted_list[position] = unsorted_list[position], unsorted_list[end]

    quicksort_step(unsorted_list, start, position-1)
    quicksort_step(unsorted_list, position+1, end)


def quicksort(unsorted_list: List[float]) -> None:
    list_length = len(unsorted_list)
    quicksort_step(unsorted_list, 0, list_length-1)
