import os
import cv2
import glob
import argparse
import shutil
from zh_wiki import zh2Hant
import codecs
from pathlib import Path

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

def main( arg ):
    input_dir = Path( args.path )
    #print(input_dir)
    output_dir = Path (args.path ).parents[0]
    #print(output_dir)
    fn = os.path.join(output_dir,"tc_{}.txt".format(input_dir.stem))
    #print(fn)
    with open(input_dir, 'r', encoding='utf-8') as f:
        try:
            contents = f.read()
        except:
            with open(input_dir, 'r', encoding='GBK') as f:
                contents = f.read()
    result = Converter(contents).output()
    f = open( fn ,"w+")
    f.write(result)
    f.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path', type=str)
	args = parser.parse_args()
	main(args)		