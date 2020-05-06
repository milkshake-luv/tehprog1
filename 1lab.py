def count_different(mas):
    print (len(set(mas)))

print("Введите последовательность чисел: ")
mas = input().strip().split()
count_different(mas)