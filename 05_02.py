def perevod(num, sistem):
    result = ''
    while num > 0:
        result = str(num%sistem) + result
        num = num//sistem
    return result

# Вопрос 2.
sum_3 = 0
for i in range(19, 34):
    sum_3 += perevod(i, 6).count('3')
print(sum_3) # Ответ: 8

# Вопрос 3.
n = 125 + 25**3 + 5**9
print(perevod(n, 5).count('0')) # Ответ: 7

# Вопрос 4.
q = 9**7 - 3**12 + 3**25 - 19
print(perevod(q, 3).count('2')) # Ответ: 12

# Вопрос 5.
w = 7 * 1296**57 - 8 * 216**30 + 35
print(perevod(w, 6).count('5')) # Ответ: 138

# Вопрос 6.
for x in range(400, 1000):
    e = 16**560 + 16**120 - x
    if perevod(e, 16).count('0') == 442:
        print(f'x = {x}')
        break # Ответ: 502

# Вопрос 7.
for x in range(1, 2031):
    r = 6**260 + 6**160 + 6**60 - x
    if perevod(r, 6).count('0') == 202:
        print(f'x = {x}')
        break # Ответ: 216

# Вопрос 8.
for x in '123456789ABCDEFGHI':
    t = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if t%18 == 0:
        print(int(x, 19)) # Ответ: 15

# Вопрос 9.
for x in '0123456789ABCDEFGHIJK':
    for y in '0123456789ABCDEFGHIJK':
        u = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        if y == '5' and u % 18 == 0:
            print(int(x, 21), x)
            break # Ответ: 3

# Вопрос 10.
for x in '0123456789AB':
    i = int(f'9A87{x}21', 12) + int(f'2{x}681', 14) - int(f'1{x}2F4', 16)
    if i % 3 == 0:
        print(int(x, 12), i//3) # Ответ: 9846242