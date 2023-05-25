import sys
import re

dadeganAmozesh=sys.argv[1]
dadeganTest= sys.argv[2]
masirKhorogi = sys.argv[3]

f = open(dadeganAmozesh,'r')
'''
f = open('E:\prj\data1.txt','r')
'''
alfa = 1
zedTekrarSet = set()

allWords = []
list_of_spam_words = []
list_of_ham_words = []

while True:
    x = f.readline()
    x=x.strip()
    if x =='':break
    x = x.split()

    for i in range(len(x)):
        x[i] = re.sub('\W+', '',x[i])
    
    if x[0] == 'spam':
        x.pop(0)
        list_of_spam_words += x
    else:
        x.pop(0)
        list_of_ham_words += x

    allWords += x

P_spam = len(list_of_spam_words)/len(allWords)
P_ham = len(list_of_ham_words)/len(allWords)
zedTekrarSet.update(allWords)
N_vocabulary = len(zedTekrarSet)

N_spam = len(list_of_spam_words)
N_ham = len(list_of_ham_words)
print("Pspam :", P_spam,"Pham :", P_ham,"Nvolcab  :  ", N_vocabulary)
print("nspam:  ", N_spam,"nham :   ",N_ham)
zedTekrarSet.clear()

f = open(dadeganTest,'r')
g = open(masirKhorogi,'w')
#f = open('E:\prj\data2.txt','r')
#g = open('E:\prj\data3.txt','w')


spam_sum = 0
ham_sum = 0
spam = 'spam	'
ham = 'ham	'
while True:
    x = f.readline()
    y = x
    x=x.strip()
    if x =='':break
    x = x.split()

    for i in range(len(x)):
        x[i] = re.sub('\W+', '',x[i])
    
    spam_sum = 0
    ham_sum = 0
    for val in x:
        N_wi_spam = list_of_spam_words.count(val)
        N_wi_ham = list_of_ham_words.count(val)
        print("Nspam :  ",N_wi_spam,"Nham", N_wi_ham)
        spam_sum += (N_wi_spam + alfa)/(N_spam + N_vocabulary)
        ham_sum += (N_wi_ham + alfa)/(N_ham + N_vocabulary)   

    #print(spam_sum)
    P_wi_spam = P_spam * spam_sum
    P_wi_ham = P_ham * ham_sum
    
   # print(P_wi_spam,P_wi_ham)
    if(P_wi_spam > P_wi_ham):
        g.write(spam+y)

    else:
        g.write(ham+y)

