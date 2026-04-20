import random


def random_numbers(count, low=0, high=100):
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
    random_list = random_numbers(200)
    sorted_random = selection_sort(random_list)

    print("--- Test na náhodném seznamu  ---")
    print(f"Původní seznam:  {random_list}")
    print(f"Seřazený seznam: {sorted_random}")
    sorted_random_bub = bubble_sort(random_list)
    print(f"Seřazený seznam: {sorted_random_bub}")

if __name__ == "__main__":
    main()