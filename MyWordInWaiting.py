import time as t

def say(Word, TimeForOneSimbol):
    Len = len(Word)
    for i in range(Len):
        SymbolNow = Word[i]
        print(SymbolNow, end='', flush=True)
        t.sleep(int(TimeForOneSimbol) / 100)
    print()
    print('-----------------------------------------------')

while True:
    print('Введите ваше слово ниже:')
    word = input('> ')
    print('Теперь введите промежуток между буквами (в миллисекундах)')
    time = input('> ')
    say(word, time)