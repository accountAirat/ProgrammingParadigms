def sort_list_imperative(numbers: list):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def sort_list_declarative(numbers: list):
    return sorted(numbers, reverse=True)


my_list = [1, 20, -3, 4, 55, 6, 7, 28]
print(my_list)
print(sort_list_declarative(my_list))
print(my_list)
print(sort_list_imperative(my_list))
