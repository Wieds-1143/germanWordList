from collections import Counter
import spacy
from spacy import displacy
import csv
import sys

def cmd_pamarators():
    """This function parses the comand line arguments.
        expected use is for this function to return the values for the text
        and exclusion words files.
        -h will work to provide help."""
    in_file = ""
    excluded_file = ""
    if len(sys.argv) == 1 or sys.argv[1] == '-h' :
        print("This program will take in a german text and output 30 most frequent words with their english translation. the parameters are -in <text file> -ex <excluded word file>")
        return "", ""

    if sys.argv[1] == "-d":
        return "text.txt", "known_words.txt"
    i =1
    while i < len(sys.argv):
        if sys.argv[i] == '-in':
            in_file = sys.argv[i+1]
            i += 1
        elif sys.argv[i] == '-ex':
            excluded_file = sys.argv[i+1]
            i += 1
        i += 1
    
    
    return in_file, excluded_file



###Start of the program
input_file, excluded_words_file = cmd_pamarators()

if input_file == "":
    exit()

text = ''
try:
    with open(input_file, 'r') as file:
        text = file.read().replace('\n', '')
except OSError:
    print("invalid input file: program exiting")
    exit()
known_words = []
try:
    with open(excluded_words_file, 'r') as file:
        known_words = file.read().split("\n")
except OSError:
    print("no known word file found \n\n")
nlp = spacy.load("de_core_news_sm")
doc = nlp(text)
words = []
word_count = {}

for token in doc:

    if token.dep_ == 'svp':
        words.append( token.lemma_ + token.head.lemma_)
        words.remove(token.head.lemma_)
    elif token.dep_ == 'punct':
        continue
    elif token.dep_ == 'sb':
        continue
    else: 
        words.append( token.lemma_)

for i in range(len(words)-1,-1,-1):
    if words[i] in known_words:
        words.pop(i)



ordered_words = Counter(words).most_common(30)

word_list = [t[0] for t in ordered_words]

with open('De->En_Dict.txt', newline='') as csvfile:
    translator = csv.reader(csvfile, delimiter='\t', quotechar='|')
  
    for row in translator:
        if row[0][0] == '#':
            continue
        if row[0] in word_list:
            print(row)
