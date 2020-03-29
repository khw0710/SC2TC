from zh_wiki import zh2Hant
import codecs

class Converter(object):
    def __init__(self, word):
        self.result = ""
        self.translate(word)
    def translate(self, char):
        for c in char:
            if c in zh2Hant:
                self.result += zh2Hant[c]
            else:
                self.result += c
    def output(self):
        return self.result



with open("01.txt", 'r', encoding='utf-8') as f:
    try:
        contents = f.read()
    except:
        with open("01.txt", 'r', encoding='GBK') as f:
            contents = f.read()

result = Converter(contents).output()
f = open("01result.txt","w+")
f.write(result)
f.close()
 