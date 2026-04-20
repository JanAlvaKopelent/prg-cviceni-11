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
    nums = list(numbers)
    n = len(nums)

    plt.ion()
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(nums)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(nums)), nums, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    plt.ioff()
    plt.show()

    return nums

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


if __name__ == "__main__":
    main()