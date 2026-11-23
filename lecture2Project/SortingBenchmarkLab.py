import random
import time


# 1. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 2. Merge Sort
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


# 3. Quick Sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


sizes = [1000, 10000, 100000]

for n in sizes:
    sorted_data = list(range(n))
    reversed_data = list(range(n, 0, -1))
    random_data = list(range(n))
    random.shuffle(random_data)

    cases = [
        ("Sorted", sorted_data),
        ("Reversed", reversed_data),
        ("Random", random_data),
    ]


    for case_name, base_data in cases:
        print(f"\n--- {case_name} ---")

        # Insertion Sort 
        if not (n == 100000 and case_name in ["Reversed", "Random"]):
            data = base_data.copy()
            start = time.perf_counter()
            insertion_sort(data)
            ins_time = (time.perf_counter() - start) * 1000
            print(f"Insertion Sort : {ins_time:.3f} ms")
        else:
            print("Insertion Sort : Skipped (too slow for n=100000)")

        # Merge Sort
        data = base_data.copy()
        start = time.perf_counter()
        merge_sort(data)
        merge_time = (time.perf_counter() - start) * 1000
        print(f"Merge Sort     : {merge_time:.3f} ms")

        # Quick Sort
        data = base_data.copy()
        start = time.perf_counter()
        quick_sort(data)
        quick_time = (time.perf_counter() - start) * 1000
        print(f"Quick Sort     : {quick_time:.3f} ms")


        data = base_data.copy()
        start = time.perf_counter()
        sorted(data)
        py_time = (time.perf_counter() - start) * 1000
        print(f"Python sorted(): {py_time:.3f} ms")