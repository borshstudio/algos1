import time
import random
import matplotlib.pyplot as plt

# ===============================
#  O(1)
# ===============================

def f01_access_middle(a):
    return a[len(a) // 2]


# ===============================
#  O(log n)
# ===============================

def f03_binary_search(a, key):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if a[m] == key:
            return m
        elif a[m] < key:
            lo = m + 1
        else:
            hi = m - 1
    return -1


# ===============================
#  O(n)
# ===============================

def f06_linear_search(a, key):
    for i, x in enumerate(a):
        if x == key:
            return i
    return -1


# ===============================
#  O(n log n)
#  Merge sort
# ===============================

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    left = merge_sort(a[:m])
    right = merge_sort(a[m:])
    return merge(left, right)

def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


# ===============================
#  O(n^2)
#  Bubble sort
# ===============================

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


# ===============================
#  O(n^2 log n)
#  Three-sum with binary search
# ===============================

def three_sum_bsearch(a, target):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            need = target - a[i] - a[j]
            if f03_binary_search(a[j+1:], need) != -1:
                return True
    return False


# ===============================
#  O(2^n)
#  Fibonacci naive
# ===============================

def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# -----------------------------------
#  TIME MEASUREMENT
# -----------------------------------

def measure(func, generator, n):
    a = generator(n)
    t1 = time.perf_counter()
    func(a)
    t2 = time.perf_counter()
    return t2 - t1


# -----------------------------------
#  MAIN EXPERIMENT
# -----------------------------------

functions = {
    "O(1) access middle": (lambda n: list(range(n)), lambda a: f01_access_middle(a)),
    "O(log n) binary search": (lambda n: list(range(n)), lambda a: f03_binary_search(a, -1)),
    "O(n) linear search": (lambda n: list(range(n)), lambda a: f06_linear_search(a, -1)),
    "O(n log n) merge sort": (lambda n: [random.randint(0, 1_000_000) for _ in range(n)], lambda a: merge_sort(a)),
    "O(n^2) bubble sort": (lambda n: [random.randint(0, 1_000) for _ in range(n)], lambda a: bubble_sort(a)),
}

sizes = [10, 100, 300, 1000, 3000, 5000]

for name, (gen, func) in functions.items():
    times = []
    print(f"\n=== {name} ===")
    for n in sizes:
        if name == "O(n^2) bubble sort" and n > 2000:
            break
        t = measure(func, gen, n)
        times.append(t)
        print(f"n={n}   time={t:.6f} sec")

    # графики
    plt.figure()
    plt.plot(sizes[:len(times)], times, marker='o')
    plt.title(name)
    plt.xlabel("n")
    plt.ylabel("Time (sec)")
    plt.grid(True)
    plt.show()