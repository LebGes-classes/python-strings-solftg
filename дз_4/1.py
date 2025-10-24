text = " " + input("Введите текст ") + " "
word = ""
result_text_1 = ""

for i in range(len(text)-1, -1, -1):
    if text[i] == " ":
      if word != "":
        word += " "
        result_text_1 += word
        word = ""
    else:
       word += text[i]

result_text_2 = ""
word1 = ""


for symb in text:
    if symb == " ":
      if word1 != "":
        word1 += " "
        result_text_2 = word1 + result_text_2
        word1 = ""
    else:
       word1 += symb

print(result_text_2)
print(result_text_1)

       
      
    

      


        
