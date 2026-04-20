import random


def random_numbers(count, low=0, high=1000):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(numbers):
    nums = list(numbers)
    n = len(nums)

    for num in range(n):
        min_idx = num

        for j in range(num + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[num], nums[min_idx] = nums[min_idx], nums[num]

    return nums


import matplotlib.pyplot as plt


def bubble_sort(numbers):
    arr = list(numbers)
    n = len(arr)

    plt.ion()
    fig, ax = plt.subplots()
    bars = ax.bar(range(n), arr, color="steelblue")
    ax.set_title("Bubble Sort")
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                bars[j].set_height(arr[j])
                bars[j + 1].set_height(arr[j + 1])

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

    plt.ioff()
    plt.show()

    return arr

def main():
    short_list = [5, 1, 4, 2, 8]
    sorted_short = selection_sort(short_list)

    print("--- Test na krátkém seznamu ---")
    print(f"Původní seznam:  {short_list}")
    print(f"Seřazený seznam: {sorted_short}\n")

    random_list = random_numbers(20)
    sorted_random = selection_sort(random_list)

    print("--- Test na náhodném seznamu (20 čísel) ---")
    print(f"Původní seznam:  {random_list}")
    print(f"Seřazený seznam: {sorted_random}")

    random_list2 = random_numbers(10)

    print(f"Původní seznam: {random_list2}")

    sorted_random_bub = bubble_sort(random_list2)

    print(f"Seřazený seznam: {sorted_random_bub}")

if __name__ == "__main__":
    main()