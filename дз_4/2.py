from re import *

text = input("Введите текст ")
words = findall(r"[A-Za-z]+", text)
k = 0

for word in words:
    if len(word) > k:
        k = len(word)

bytes_list = list(text.encode("utf-8"))

for i in range(len(bytes_list)):
    utf_code_word = bytes_list[i]
    if 65 <= utf_code_word <= 90:
        bytes_list[i] = (utf_code_word - 65 + k) % 26 + 65 #%26 т.к.алфавит циклический
    elif 97 <= utf_code_word <= 122:
        bytes_list[i] = (utf_code_word - 97 + k) % 26 + 97
    
redone_text = bytes(bytes_list).decode("utf-8")

print(redone_text)
print(k)