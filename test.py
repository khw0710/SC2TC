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

result = Converter(open("test.txt", encoding="utf-8").read()).output()

f = open("result.txt","w+")
f.write(result)
f.close() 