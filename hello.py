from datetime import date

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    today = date.today().strftime("%B %d, %Y")
    print(f"Hello Earth! Today's date is {today}.")


if __name__ == "__main__":
    main()
