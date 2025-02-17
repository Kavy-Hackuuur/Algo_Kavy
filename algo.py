INSERTION_SORT = [
"Insertion Sort Algorithm:-",
"for j <- 2 to n:",
"    key <- Arr[j]",
"    i <- j - 1",
"    while i > 0 and Arr[i] > key:",
"        Arr[i + 1] <- Arr[i]",
"        i <- i-1",
"    Arr[i + 1] <- key"
]

BUBBLE_SORT = [
"Bubble Sort Algorithm:-",
"for i <- 1 to n:",
"    for j <- 1 to n - i:",
"        if Arr[j] > Arr[j + 1]:",
"            Arr[j] <--> Arr[j + 1] (Swap)"
]

SELECTION_SORT = [
"Selection Sort Algorithm:-",
"for i <- 1 to n - 1:"
"    min <- i",
"    for j <- i + 1 to n:",
"        if Arr[i] < Arr[min]:",
"            min <- i",
"    Arr[min] <--> Arr[i] (Exchange)"
]

MERGE_SORT = [

]

JUMP_SEARCH = [
"step <- Square_root(n)",
"prev = 0",
"while Arr[Minimum(step, n) - 1] < x:",
"    prev <- step",
"    step <- step + Square_root(n)",
"    if prev >= n:",
"        return -1",
"while arr[int(prev)] < x:",
"    prev <- prev + 1",
"    if prev == min(step, n):",
"        return -1",
"if Arr[prev] == x:",
"    return prev"
]

BINARY_SEARCH = [
"while left ≤ right:",
"    middle <- (left + rigth) / 2",
"    if Arr[middle] == key:",
"        return middle",
"    else if key < Arr[middle]:",
"        right <- middle - 1",
"    else:",
"        left <- middle + 1",
"return -1"
]

LINEAR_SEARCH = [
"n <- length(Arr)",
"for i <- 1 to n:",
"    if Arr[i] == key:",
"        return i"
]
