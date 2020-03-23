import re
 
punctuation = '!,;:?"\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip().lower()
 
text = " Hello, world!  "
print(removePunctuation(text))