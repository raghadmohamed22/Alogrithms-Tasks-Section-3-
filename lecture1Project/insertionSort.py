import random
import time

# 1. Implement: Insertion Sort
def insertion_sort(arr):
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons, shifts


# Merge Sort  للمقارنة
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 2 و 3. التجربة والتحليل لقيم n من 100 إلى 5000
sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

for n in sizes:
    sorted_list = list(range(n))
    reverse_list = list(range(n, 0, -1))
    random_list = list(range(n))
    random.shuffle(random_list)

    cases = [
        ("Sorted", sorted_list),
        ("Reverse", reverse_list),
        ("Random", random_list),
    ]

    print(f"\n--- n = {n} | O(n) = {n} | O(n^2) = {n * n} ---")

    for name, data in cases:
        # Insertion Sort
        arr_copy = data.copy()
        start = time.time()
        comps, shifts = insertion_sort(arr_copy)
        ins_time = (time.time() - start) * 1000

        # Merge Sort
        
        m_start = time.time()
        merge_sort(data.copy())
        m_time = (time.time() - m_start) * 1000

        print(
            f"{name:7s} -> "
            f"Insertion: {ins_time:.3f} ms | "
            f"Merge: {m_time:.3f} ms | "
            f"Comparisons: {comps} | "
            f"Shifts: {shifts}"
        )