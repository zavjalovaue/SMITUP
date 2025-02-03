# Вопрос 3.
def summa(my_list):
    s = 0
    for i in my_list:
        s += i
    return s
print(summa([3, 4, 6]))

# Вопрос 4.
def palindrom(s):
    if s == s[::-1]:
        return "Это палиндром"
    else:
        return "Это не палиндром"
print(palindrom("civic"))

# Вопрос 5.
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
print(factorial(0))

# Вопрос 6.
def max_num(some_list: list):
    return max(some_list)
print(max_num([3, 4, 6]))

# Вопрос 7.
def sum_digits(n):
    summ = 0
    for i in str(n):
        summ += int(i)
    return summ
print(sum_digits(91))

# Вопрос 8.
def count_letters(text):
    letters = 'EeYyUuOoAaIi'
    letters_count = {v: 0 for v in letters}
    
    for char in text.lower():
        if char in letters_count:
            letters_count[char] += 1
    return letters_count

result = count_letters('Intersting text')
print(", ".join(f"'{v}': {count}" for v, count in result.items()))
