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

SELECTION_SORT = [
        "for i in range(n):",
        "   min_idx = i",
        "   for j in range(i + 1, n):",
        "       if self.data[j] < data[min_idx]:",
        "           min_idx = j",
]

MERGE_SORT = [

]
