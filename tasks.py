# Задание 1. Сумма чисел в списке
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_list([1,2,3,4]))  


# Задание 2. Подсчет гласных
word = input("Введите слово: ")
vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1
print(f'Гласны: {count}')
