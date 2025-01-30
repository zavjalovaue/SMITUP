# Задание 1
lower = 4
upper = 15

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for number in range(lower, upper + 1):
    if is_prime(number):
        print(number)

# Задание 2
start = 500000
procent = 23
time_periods = [15, 36, 66]
target_amount = 1300000
months = 0

def calculate_future_value(start, aprocent, months):
    monthly_rate = aprocent / 12 / 100
    future_value = start * (1 + monthly_rate) ** months
    return future_value

for months in time_periods:
    future_value = calculate_future_value(start, procent, months)
    print(f"Через {months} месяцев у Ивана будет: {future_value:.2f} рублей")

while start < target_amount:
    start = calculate_future_value(500000, procent, months)
    months += 1

print(f"\nИван сможет сыграть свадьбу за {months} месяцев.")

# Задание 3
lst=[1, 2, 16, 5, 77]
def find_useless_number(lst):
    max_number = max(lst)
    length = len(lst)
    useless_number = (max_number / length) ** 2
    even_sum = sum(num for num in lst if num % 2 == 0)
    return useless_number + even_sum
print(find_useless_number(lst))

# Задание 4
list1 = [10, 20, 10, 20, 30, 40, 30, 50]
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates(list1))
