T = int(input())

def is_odd(number: int) -> bool:
    return number % 2 == 1

for test_case in range(1, T + 1):
    numbers = list(filter(is_odd, list(map(int, input().split()))))

    print('#' + str(test_case), end=" ")
    print(sum(numbers))