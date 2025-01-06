INSERTION_SORT = [
    "for i in range(1, n):",
        "   key = data[i]",
        "   j = i - 1",
        "   while j >= 0 and key < data[j]:",
        "       data[j + 1] = data[j]",
        "       data[j + 1] = key"
]

BUBBLE_SORT = [
    "for i in range(n):",
    "   for j in range(n - i - 1):",
    "       if data[j] > data[j + 1]:",
    "           data[j], data[j + 1] = data[j + 1], data[j]"
]   