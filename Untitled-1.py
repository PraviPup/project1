a = input('Введіть текст:')
while a == 'Так':
    with open("ooo.txt", "w") as f:
        f.write(a)
    with open("ooo.txt", "r") as f:
        f = f.read()
        print(f)
    a = input('Введіть текст:')

print('Ладно.')
#ешкере
