import re

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
        lexemes = re.findall(r'\b\d+\b', block)
        for lexeme in lexemes:
            nomer_str = ' '.join(slovarik[c] for c in lexeme)
            schetchik_chisel = {c: lexeme.count(c) for c in lexeme}
            print(f"Цифры прописью: {nomer_str}, Количество цифр: {len(lexeme)}, Используемые цифры и их количество: {schetchik_chisel}")
        block = f.read()
