
import re
import sys
if len(sys.argv)<2:
	print("Provide file name\n")
	exit(0)
# with open("F:\\NLP\\assignment2regularexpression_18693\\Assignment 2\\Development Set.txt", 'r') as content_file:
with open(sys.argv[1], 'r') as content_file:    
    content = content_file.read()
#print(content)

# compiling different regular expressions for content
#counting paragraph
count_para=re.compile("\n\n")
#counting words
count_word=re.compile("\s+")
no_of_para=len(count_para.findall(content))
no_of_word=len(count_word.findall(content))+1 #counting first word
# counting various cases:
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
websites = "[.](com|net|org|io|gov)"
acronym="([A-Za-z][.][A-Za-z][.](?:[A-Za-z][.])?)"

acr=re.compile(acronym)
pre=re.compile(prefixes)
suf=re.compile(suffixes)
web=re.compile(websites)

#1) Number of paragraphs, sentences, and words contained in the article.
# no. of "." in all acronyms
acr_l=acr.findall(content)
#print(acr_l)
count_dots=0
for i in acr_l:
    #print(i)
    count_dots+=len(i)/2
    #print(count_dots)
# no. of "." in all prefixes
len_pre=len(pre.findall(content))

# no. of "." in all suffixes
len_suf=len(suf.findall(content))

# no. of "." in all websites
len_web=len(web.findall(content))

# counting all "." in the document
dots=re.compile("[\.?!]")
len_dots=len(dots.findall(content))
# getting count of sentences:
no_of_sent=len_dots-(count_dots+len_pre+len_suf+len_web)

print("No of Paragraph =",no_of_para)
print("No of Sentences =",int(no_of_sent))
print("No of Words =",no_of_word)

#2) Given a word as input, number of sentences starting with the word.
inp=input("Enter a word to count number of sentences starting with this word ")
#print(inp)
word=inp.lower()
WORD=inp.upper()
#print(word[0])
upper=word[0].upper()
lower=word[0].lower()
count_word_start=re.compile("^"+"(?:"+upper+word[1:]+"|"+WORD+")[^A-Za-z0-9]|\. (?:"+upper+word[1:]+"|"+WORD+")[^A-Za-z0-9]|\; (?:"+upper+word[1:]+"|"+WORD+")[^A-Za-z0-9]|\? (?:"+upper+word[1:]+"|"+WORD+")[^A-Za-z0-9]|\n\n(?:"+upper+word[1:]+"|"+WORD+")[^A-Za-z0-9]")
li=count_word_start.findall(content)
if(len(li)==0):
	print("No sentence start with",inp)
else:
	print("No. of sentences starting with",inp,"=",len(li))


#3) Given a word as input, number of sentences ending with the word.
inp=input("Enter a word to count no. of sentences ending with this word ")
word=inp.lower()
WORD=word.upper()
#print(word[0])
upper=word[0].upper()
lower=word[0].lower()

count_word_end=re.compile("[^A-Za-z0-9]["+lower+"|"+upper+"]"+word[1:]+"[^a-zA-Z0-9]"+"$"+"|"+"[^A-Za-z0-9]["+lower+"|"+upper+"]"+word[1:]+"\."+"|"+ 
                          "[^A-Za-z0-9]["+lower+"|"+upper+"]"+word[1:]+"\?"+"|"+ lower+word[1:]+"\;"+"|"+lower+word[1:]+"\n\n"+"|"+
                          "[^A-Za-z0-9]["+lower+"|"+upper+"]"+word[1:]+"\.")

li=count_word_end.findall(content)
if(len(li)==0):
	print("No sentence ends with",inp)
else:
	print("No. of sentences ending with",inp,"=",len(li))

#4) Given a word as input, count of that word in the input file.
inp=input("Enter a word to count occurences ")
word=inp.lower()
WORD=word.upper()
#print(word[0])
upper=word[0].upper()
lower=word[0].lower()
acronym="([A-Za-z][.][A-Za-z][.](?:[A-Za-z][.])?)"
#print(lower)
count_word_All=re.compile("[^a-zA-Z0-9]+"+"(?:["+lower+"|"+upper+"]"+word[1:]+"|"+WORD+")[^a-zA-Z0-9]")
li=count_word_All.findall(content)
# print(count_word_All.findall(content))
if(len(li)==0):
	print("No sentence contains ",inp)
else:
	print("No. of sentences containing ",inp,"=",len(li))