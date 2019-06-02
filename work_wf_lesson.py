with open('referat.txt', 'r', encoding='utf8') as text:
    text = text.read()
    print(len(text))

text = text.replace('\n', ' ').replace('.', '!')
text = text.split(' ')
punctuation = [',', '.', ':', '«', '»', '!', ' ']

for element in text:
    if element == punctuation:
        del text[element]

print(text)
print(len(text))