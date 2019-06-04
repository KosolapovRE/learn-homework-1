with open('referat.txt', 'r', encoding='utf8') as a:
    text = a.read()

text_len = str(len(text))
text = text.replace('.', '!')
text_list_len = str(len(text.split(' ')))

with open('referat2.txt', 'w', encoding='utf8') as new_text:
    new_text.write(text)
    new_text.write('\n')
    new_text.write(text_len)
    new_text.write('\n')
    new_text.write(text_list_len)
        
        
