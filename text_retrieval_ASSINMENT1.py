import operator
import string
import re
with open('example.txt','r') as f:
    file2 = (f.read()).lower()
    pattern_re = re.search(r'\b[a-z]{3,16}\b',file2)

line_number = input("Please Enter the line number = ")
word_number = input("Please Enter the word number = ")

with open("example.txt") as myfile:
    the = myfile.readlines()[line_number].split()[word_number]
    print("For line number {:<1} and word number {:<1} The word is = {:<1}".format(line_number,word_number,the))


punct =[]
print punct
for p in string.punctuation:
    file2 = file2.replace(p, "").replace('\n', " ").replace("  ", " ")

word_values = {}

for word in file2.split(" "):
    if word in word_values.keys():
        word_values[word] += 1
    else:
        word_values[word] = 1


words = [word for line in file2 for word in line.split()]

#print book
num = float(len(words))
num1 = len(words)
print("The Total number of words in text file is :{} \n ".format(num1))
sorted_hist = sorted(word_values.items(), key=operator.itemgetter(1))

for idx, item in enumerate(sorted_hist[:-11:-1]):
    word, count = item
    print('{:<2}:  {:<5}  {:>1}'.format(idx + 1, word, count))
    print("The probabity for {:<1} '{:<2}' = {:>1} \n".format(idx+1,word,float(count)/num))
#print line