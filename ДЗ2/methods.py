def method1(inpstr, inpmethod):
    if inpmethod == 1:
        return inpstr.upper()
    if inpmethod == 2:
        return inpstr.lower()
    if inpmethod == 3:
        return inpstr.capitalize()


def method2(inpstr, inpmethod):
    if inpmethod == 1:
        what = str(input("Что найти в строке: "))
        return inpstr.find(what)
    if inpmethod == 2:
        what = str(input("Что заменить: "))
        what2 = str(input("На что заменить: "))
        return inpstr.replace(what, what2)
    if inpmethod == 3:
        what = str(input("Что посчитать в строке: "))
        return inpstr.count(what)


def method3(inpstr, inpmethod):
    if inpmethod == 1:
        what = str(input("По какому элементу разделять: "))
        return inpstr.split(what)
    if inpmethod == 2:
        what = str(input("Через что перечислить строки: "))
        return inpstr.join(what)


def method4(inpstr, inpmethod):
    if inpmethod == 1:
        return inpstr.isdigit()
    if inpmethod == 2:
        return inpstr.isalpha()
    if inpmethod == 3:
        chr = str(input("Какие символы надо убрать с концов? "))
        return inpstr.strip(chr)


def method5(inpstr):
    return "".join([i.capitalize() for i in inpstr.strip().split("_")])


lvltext = ['Уровень 1. Вы можете выбрать 1 из 3 методов изменения строки. 1-й: upper().Он переведет все символы строки в верхний регистр. Второй - lower(). Он, наоборот, переводит символы в нижний регистр. 3-й capitalize() переводит первый символ строки в верхний регистр, остальные - в нижний.\nПример: hELLO WORLD.capitalize() = Hello world\nhElLO wOrLd.capitalize() = hello world\nhElLO wOrLd.capitalize() = HELLO WORLD\nДай мне строку и номер метода.',
           'уровень 2. Вы можете выбрать 1 из 3 методов работы со строкой. 1-й: find(s). Он ищет позицию первого вхождения символа, введенного в скобки и возвращает индекс этого вхождения. 2-й: replace(s1, s2). Он заменяет одну последовательность символов строки на другую. 3-й: count(s1, s2). Он считает, сколько раз в строке встречается подстрока.\nПример: Ботать это круто. Очень круто.find(круто) = 11\nБотать это круто. Очень круто.replace(круто, к) = Ботать это к. Очень к\nБотать это круто. Очень круто.count(круто) = 2',
           'Уровень 3. Вы можете выбрать 1 из 2 методов работы со строкой. 1-й: split(argument). Он разделяет строку на подстроки и объединяет их в массив. В качестве разделителя он использует аргумент. 2-й: join(argument). Он применяется к строке, вставляя ее между элементами списка строк argument. Также можно указать методу значение 3, тогда сначала произойдет разделение введенной строки по \nПример: 1,2,3,4.split(,) = [1, 2, 3, 4]\n",".join(["1", "2", "3", "4"]) = "1,2,3,4"',
           'Уровень 4. Вы можете выбрать 1 из 3 методов работы со строкой. 1-й isdigit(). Возвращает True усли все символы в строке - цифры и есть хоть 1 символ, False если это не так. 2-й метод - .isalpha(), он возвращает True если все символы - буквы и есть хотя бы 1 символ, False в обратном случае. 3-й: .strip(char) возвращает строку, с обрезанными с обеих сторон символами char. \nПример: "12345".isdigit() = True, "123 456".isdigit() = False \n"abcd".isalpha() = True, "abc1_def".isalpha() = False \n"   abc   ".strip() = "abc", "__-_abc_-__".strip("_") = "-_abc_-"',
           'Уровень 5. У введенной строки удалятся пробелы с обеих сторон, разделится по "_", все слова станут с большой буквы и склеятся']


   
while True:
    lvl = int(input("Выберите уровень от 1 до 5, 0 - выход: "))
    print(lvltext[lvl-1])
    
    stringconv = str(input())
    if lvl == 1:
        method = int(input())
        print(method1(stringconv, method))
    elif lvl == 2:
        method = int(input())
        print(method2(stringconv, method))
    elif lvl == 3:
        method = int(input())
        print(method3(stringconv, method))
    elif lvl == 4:
        method = int(input())
        print(method4(stringconv, method))
    elif lvl == 5:
        print(method5(stringconv))
    elif lvl == 0:
        print("Завершение")
        break
        
    
