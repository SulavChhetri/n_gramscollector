import pandas as pd
import csv
from collections import defaultdict
import json


n_grams_40 = []
statelist= []

with open('./files/stopwords.txt', 'r')as file:
    lines = [line.rstrip('\n') for line in file]

with open('./files/states.json')as file:
    statedict=json.load(file)

for item in statedict:
    statelist.append(item['State'])


def stateExtracter(note):
    for i in range(1,4):
        x= ngramcreator(note,i)
        for item in x:
            if item in statelist:
                return item

def takeSecond(elem):
    return elem[1]

def stopwordsremover(sentence):
    nostopword_sentence =list()
    for item in sentence.split():
        if not item.lower() in lines:
            nostopword_sentence.append(item)
    return nostopword_sentence

def ngramcreator(strings,n_grams):
    finallist = []
    finalstring = ''
    splitlist = strings.split()
    n_grams_range = len(splitlist)-n_grams+1
    if (len(strings.split())<n_grams):
        return [strings]
    else:
        for x in range(n_grams_range): 
            for i in range(n_grams):  
                l =[]
                for items in splitlist[x+i]:
                    l.append(items.strip(',.?-&*():'))
                finalstring =finalstring+' '+''.join(l)
            finallist.append(finalstring.lstrip())
            finalstring = ''
        return finallist

def n_grams():
    bidict = defaultdict(int)
    tridict = defaultdict(int)
    data = pd.read_csv('./files/3_govt_urls_state_only.csv')
    data = data['Note']
    for item in data:
        note = item.split("--")[0]
        nostopword_note = ' '.join(stopwordsremover(note))
        for number in range(2,4):
            n_gram = ngramcreator(nostopword_note,number)
            for i in n_gram:
                if i not in statelist:
                    if number==2:
                        bidict[i]+=1
                    else:
                        tridict[i]+=1

    templist1 = sorted(bidict.items(),key=takeSecond,reverse=True)[:20]
    templist2 = sorted(tridict.items(),key=takeSecond,reverse=True)[:20]
    for item in templist1:
        n_grams_40.append(item[0])
    
    for item in templist2:
        n_grams_40.append(item[0])

def main():
    n_grams()
    data = pd.read_csv('./files/3_govt_urls_state_only.csv')
    data = data['Note']
    keylist= defaultdict(list)
    statelist = defaultdict(str)
    for item in data:
        note = item.split("--")[0]
        nostopword_note = ' '.join(stopwordsremover(note))
        state = stateExtracter(nostopword_note)
        if state!=None:
            for i in range(2,4):
                n_gram = ngramcreator(nostopword_note,i)
                for item in n_gram:
                    if item in n_grams_40:
                        if item not in keylist[note]:
                            keylist[note].append(item)
                            statelist[note]=state

    with open('n_output.csv','w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(["Topic","State","Note"])
        for key in keylist.keys():
            writer.writerow([f"{keylist[key]}",f"{statelist[key]}",f"{key}"])


main()