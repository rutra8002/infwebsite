def is_palindrome_ez(arr):
    if arr == reverse_array(arr):
        return True
    else:
        return False


def reverse_array_ez(arr):
    return arr[::-1]

def is_palindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False
    return True

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(is_palindrome(arr))  # Sprawdzenie, czy tablica jest palindromem
print(reverse_array(arr))  # Odwracanie tablicy
print(bubble_sort(arr.copy()))  # Sortowanie bąbelkowe
print(selection_sort(arr.copy()))  # Sortowanie przez wybór
