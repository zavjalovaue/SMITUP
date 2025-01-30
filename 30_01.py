import string
# Задание 1
s = input()
s = s.lower()
if s == s[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")

# Задание 2
stroka = input()
translator = str.maketrans('', '', string.punctuation)
print(stroka.translate(translator))

# Задание 3
text = input()

def count_letters(text):
    letters = 'аеёиоуыэюя'
    letters_count = {v: 0 for v in letters}
    
    for char in text.lower():
        if char in letters_count:
            letters_count[char] += 1
    return letters_count

result = count_letters(text)
print(", ".join(f"'{v}': {count}" for v, count in result.items()))