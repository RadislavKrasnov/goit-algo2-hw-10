import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt


def partition_lomuto(array, start_index, end_index):
    pivot_value = array[end_index]
    smaller_element_boundary = start_index - 1
    
    for current_index in range(start_index, end_index):
        if array[current_index] <= pivot_value:
            smaller_element_boundary += 1
            array[smaller_element_boundary], array[current_index] = array[current_index], array[smaller_element_boundary]
    
    array[smaller_element_boundary + 1], array[end_index] = array[end_index], array[smaller_element_boundary + 1]
    
    return smaller_element_boundary + 1


def randomized_quick_sort(array):
    def quick_sort_recursive(start_index, end_index):
        if start_index < end_index:
            random_pivot_index = random.randint(start_index, end_index)
            array[random_pivot_index], array[end_index] = array[end_index], array[random_pivot_index]
            pivot_final_index = partition_lomuto(array, start_index, end_index)
            quick_sort_recursive(start_index, pivot_final_index - 1)
            quick_sort_recursive(pivot_final_index + 1, end_index)
   
    quick_sort_recursive(0, len(array) - 1)


def deterministic_quick_sort(array):
    def quick_sort_recursive(start_index, end_index):
        if start_index < end_index:
            middle_index = start_index + (end_index - start_index) // 2
            array[middle_index], array[end_index] = array[end_index], array[middle_index]
            pivot_final_index = partition_lomuto(array, start_index, end_index)
            quick_sort_recursive(start_index, pivot_final_index - 1)
            quick_sort_recursive(pivot_final_index + 1, end_index)
    
    quick_sort_recursive(0, len(array) - 1)

array_sizes = [10_000, 50_000, 100_000, 500_000]
array_sizes = [10_000, 50_000, 100_000, 500_000]
num_repeats = 5

results_summary = []

for array_size in array_sizes:
    print(f"Розмір масиву: {array_size}")
    
    base_array = [random.randint(0, 1_000_000) for _ in range(array_size)]
    
    randomized_time = timeit.timeit(
        stmt=lambda: randomized_quick_sort(base_array.copy()),
        number=num_repeats
    ) / num_repeats
    
    deterministic_time = timeit.timeit(
        stmt=lambda: deterministic_quick_sort(base_array.copy()),
        number=num_repeats
    ) / num_repeats

    print(f"   Рандомізований QuickSort: {randomized_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд\n")

    results_summary.append({
        "size": array_size,
        "avg_randomized_s": randomized_time,
        "avg_deterministic_s": deterministic_time
    })


df = pd.DataFrame(results_summary)
df["avg_randomized_ms"] = df["avg_randomized_s"] * 1000
df["avg_deterministic_ms"] = df["avg_deterministic_s"] * 1000

plt.figure(figsize=(8, 5))
plt.plot(df["size"], df["avg_randomized_s"], marker='o', label='Randomized QuickSort')
plt.plot(df["size"], df["avg_deterministic_s"], marker='o', label='Deterministic QuickSort')
plt.xlabel("Розмір масиву (n)")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння часу: Randomized vs Deterministic QuickSort (timeit)")
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.xticks(df["size"], df["size"])
plt.tight_layout()
plt.show()
