#ВАРИАНТ 16: Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество.
slovarik = {
    '0': 'ноль',
    '1': 'раз',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пятёрочка',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}
with open('myheard.txt', 'r') as f:
    block = f.read(1024)
    while block:
        lexemes = block.split()
        for lexeme in lexemes:
            nomer_str = ''
            schetchik_chisel = {}
            for cifra in lexeme:
                if cifra.isdigit():
                    if cifra in schetchik_chisel:
                        schetchik_chisel[cifra] += 1
                    else:
                        schetchik_chisel[cifra] = 1
                    nomer_str += slovarik[cifra] + ' '
            print(f"Цифры прописью: {nomer_str}, Количество цифр: {len(lexeme)}, Используемые цифры и их количество: {schetchik_chisel}")
        block = f.read()
