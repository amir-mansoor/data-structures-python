# ****** Order of growth" **********
import time

# 😼 this is for fun you can use modules like matplotlib etc
def plot_lists(x, y):
    max_y = max(y)
    
    # Handle the case where max_y is zero
    if max_y == 0:
        scale_factor = 1  # Avoid division by zero, no need to scale since all values are 0
    else:
        scale_factor = 10 / max_y  # Scaling factor for y-axis

    for i in range(len(x)):
        bar = " " * x[i] + "|" + "*" * int(y[i] * scale_factor)
        print(f"x: {x[i]} | y: {y[i]} {bar}")


def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n-2) + fib1(n-1)

def fib2(n):
    a = 1
    b = 1

    for i in range(n):
        a,b = b, a + b

    return a

# print("Fib: ")
# for i in range(15):
#     print(fib1(i), end=", ")

# print("Fib 2: ")
# for i in range(15):
#     print(fib2(i), end=", ")

def compute_times(fn,limit):
    l = []
    for i in range(limit):
        start_time = int(round(time.time() * 1000))

        fn(i)

        end_time = int(round(time.time() * 1000))
        time_taken = end_time - start_time

        l.append(time_taken)

    return l

limit = 30
fib1_times = compute_times(fib1,limit)
fib2_times = compute_times(fib2,limit)

# print(fib1_times)
# print(fib2_times)
plot_lists(fib1_times,fib2_times)