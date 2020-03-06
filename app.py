import random

count = 4
words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
used_lit = ""

def hello():
    word  = random.choice(words)
    len_word = len(word)
    print(f'Отгадай слово из {len_word} букв')
    return word

def make_frame(word):
    len_word = len(word)
    frame = ["_" for i in range(len_word)] 
    print(' '.join(frame))
    return frame

def get_new_literal():    
    lit = input('Введите букву на английском: ')
    lit = veryficaition(lit) 
    return lit

def veryficaition(lit):
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


def checking():
    if lit  in word:
        for l in word:
            if l == lit:
                num = word.find(l)                
                summa = word.count(l)
                if summa == 1:
                    frame[num] = l
                    print(' '.join(frame)) 
                    return frame
                else:
                    for i in range(summa):
                        num = word.find(l, (num + i))
                        frame[num] = l
                    print(' '.join(frame)) 
                    return frame

                    # num2 = word.find(l, (num + 1))
                    # frame[num2] = l
                    # print(' '.join(frame)) 
                    # return frame

                
    else:
        print(' '.join(frame))
        return frame


word = hello()
frame = make_frame(word) 
while count > 0:
    if "_" not in frame:
        print("Вы угадади!")
        game = input("Хотите играть еще раз?  (y or n)  ")
        if game.startswith("y"):
            count = 4
            word = hello()
            frame = make_frame(word)
            continue
        else:
            break
    else:
        lit = None
        lit = get_new_literal()
        used_lit += lit
        if lit not in word:
            count = make_count_less(count, word)
            continue  
        lit = veryficaition(lit)        
        frame = checking()

