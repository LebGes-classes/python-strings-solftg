import re

text = input("Введите текст ")
words = re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", text)
symbols = {
    "A":"a", "B":"b", "C":"c", "D":"d", "E":"e", "F":"f", 
    "G":"g", "H":"h", "I":"i", "J":"j", "K":"k", "L":"l",
    "M":"m", "N":"n", "O":"o", "P":"p", "Q":"q", "R":"r",
    "S":"s", "T":"t", "U":"u", "V":"v", "W":"w", "X":"x",
    "Y":"y", "Z":"z", "А":"а", "Б":"б", "В":"в", "Г":"г",
    "Д":"д", "Е":"е", "Ё":"ё", "Ж":"ж", "З":"з", "И":"и", 
    "Й":"й", "К":"к", "Л":"л", "М":"м", "Н":"н", "О":"о", 
    "П":"п", "Р":"р", "С":"с", "Т":"т", "У":"у", "Ф":"ф",
    "Х":"х", "Ц":"ц", "Ч":"ч", "Ш":"ш", "Щ":"щ", "Ъ":"ъ",
    "Ы":"ы", "Ь":"ь", "Э":"э", "Ю":"ю", "Я":"я"
}


words_count = {}

for word in words:
    str_lower = ""

    for symb in word:
        if symb in symbols:
            str_lower += symbols[symb]
        else:
            str_lower += symb

    if str_lower in words_count:
        words_count[str_lower] += 1
    else:
        words_count[str_lower] = 1

list_of_words = []

for wrd, cnt in words_count.items():
    list_of_words.append((wrd, cnt))

n = len(list_of_words)

for i in range(n):
    for j in range(0, n-i-1):
        if list_of_words[j][1] < list_of_words[j + 1][1]:
            list_of_words[j], list_of_words[j + 1] = (
                list_of_words[j + 1],
                list_of_words[j]
                )
        

print("Топ 5 самых частых слов:")
for i in range(min(5, len(list_of_words))): #если меньше 5 слов чтобы не было ошибки
    word, count = list_of_words[i]
    print(word, count)
    

