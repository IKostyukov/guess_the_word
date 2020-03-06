import random

count = 4
words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
used_lit = ""

def hello():
    """Выбирает слово из списка"""
    word  = random.choice(words)
    len_word = len(word)
    print(f'Отгадай слово из {len_word} букв')
    return word

def make_frame(word):
    """Создает и выводит на экран рамку/макет _ _ _ _ ...,
     в которой нужно  открывать буквыЭЭ"""
    len_word = len(word)
    frame = ["_" for i in range(len_word)] 
    print(' '.join(frame))
    return frame

def get_new_literal():
    """Получает букву от игрока"""    
    lit = input('Введите букву на английском: ')
    lit = veryficaition(lit) 
    return lit

def veryficaition(lit):
    """Проверяет букву"""
    # print(type(lit))
    if  len(lit) > 1:
        print("Некорректный ввод/ Введите одну букву")
        print(' '.join(frame))
        return get_new_literal()
        
    elif lit.lower() not in "qwertyuiopasdfghjklzxcvbnm":
        print("Некорректный ввод/ Вы ввели не на латинице")
        print(' '.join(frame))
        return get_new_literal()

    elif lit.lower() in used_lit:
        print("Вы уже указывали эту букву/ Введите другую")
        print(' '.join(frame)) 
        return get_new_literal()

    else:
        return lit

def make_count_less(count, word):
    """Делает счетчик меньньше, и если после этого он равен нулю,
    предлагает начать заново, и если игрок выбрал "y"
    начинает игру заново"""    
    count -= 1
    if count == 0:
        print(f"Попыток больше нет. Загаданное слово {word}")
        game = input("Хотите играть еще раз?  (y or n)  ")
        if game.startswith("y"):
            count = 4
            global used_lit 
            used_lit = ""
            hello()
            global frame
            frame = make_frame(word)

            return count
    else:
        print(f'Такой буквы нет в этом слове.\nПопробуй еше - осталось {count} попытки')
        print(' '.join(frame))
        return count


def opening_lit():
    """ Открывает угаданную букву:
    Проверяет есть ли в слове введенная игроком буква.
    Если есть, то сколько находит её индекс и проверяет
    сколько всего таких букв в слове.
    Если 1, то заменяет символ подчеркивания "_ "  с таким же индексом
    в рамке на эту букву.
    """ 
    if lit  in word:
        for l in word:
            if l == lit:
                num = word.find(l)                
                summa = word.count(l)
                if summa == 1:
                    frame[num] = l
                    print(' '.join(frame)) 
                    return frame
                else: #Если больше чем 1
                      
                    for i in range(summa):
                        num = word.find(l, (num + i)) # то в цикле находит все индексы этих букв
                                                     # word.find(l, (num + 1)) ищет  в слове word 
                                                     # индекс буквы l
                                                     # начиная с индекса (num + 1), т.е. 
                                                     # после индекса первой найденной буквы l в слове 
                        frame[num] = l # и заменяет все "_" с такимиже индексами на эту букву
                    print(' '.join(frame)) 
                    return frame
                
    else:
        print(' '.join(frame))
        return frame


word = hello()
frame = make_frame(word) 
while count > 0:
    if "_" not in frame: #Проверяем не отгаданы ли уже все буквы
        print("Вы угадади!")
        game = input("Хотите играть еще раз?  (y or n)  ")
        if game.startswith("y"): #Начинаем новую игру
            count = 4
            word = hello()
            frame = make_frame(word)
            continue
        else:   #Выходим из игры
            break
    else:   #Если буквы не отгаданны
        lit = None   #Обнуляем переменную
        lit = get_new_literal()  #Полулаем новую букву
        used_lit += lit  #Добавляем новую букву в спсок использованных букв
        if lit not in word: #Если буква не в слове, уменьшаем счетчик и продолжаем цикл
            count = make_count_less(count, word)
            continue  
        # lit = veryficaition(lit)        
        else: # Если буква в слове, то вызываем функцию, для открытия буквы
            frame = opening_lit()
            

