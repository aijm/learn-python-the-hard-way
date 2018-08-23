# EXERCISE 33: While Loops



# def get_numbers(n, step):
#     i = 0
#     numbers = []
#     while i < n:
#         print(f"At the top i is {i}")
#         numbers.append(i)

#         i = i + step
#         print("Numbers now:", numbers)
#         print(f"At the bottom i is {i}")

#     print("The numbers: ")

#     for num in numbers:
#         print(num)

#     return numbers

def get_numbers(n):
    i = 0
    numbers = []
    for i in range(0, n):
        print(f"At the top i is {i}")
        numbers.append(i)

        # i = i + step
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

    return numbers

# get_numbers(6, 1)
# get_numbers(10, 2)

get_numbers(6)
get_numbers(10)