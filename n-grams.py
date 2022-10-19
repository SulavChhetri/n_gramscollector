import pandas as pd
import csv

n_grams_40 = []

with open('./files/stopwords.txt', 'r')as file:
    lines = [line.rstrip('\n') for line in file]

def takeSecond(elem):
    return elem[1]

def stopwordsremover(sentence):
    nostopword_sentence =list()
    for item in sentence.split():
        if not item.lower() in lines:
            nostopword_sentence.append(item)
    return nostopword_sentence

def ngramchecker(strings,n_grams):
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
    bigram_global ={}
    trigram_global ={}
    bidict = {}
    tridict = {}
    data = pd.read_csv('./files/3_govt_urls_state_only.csv')
    data = data['Note']
    for item in data:
        note = item.split("--")[0]
        nostopword_note = ' '.join(stopwordsremover(note))
        for number in range(2,4):
            n_gram = ngramchecker(nostopword_note,number)
            for i in n_gram:
                if number==2:
                    if i not in bidict.keys():
                        bidict[i]=1
                    else:
                       bidict[i] =bidict[i]+1
                else:
                    if i not in tridict.keys():
                        tridict[i]=1
                    else:
                       tridict[i] =tridict[i]+1

    templist1 = sorted(bidict.items(),key=takeSecond,reverse=True)[:20]
    templist2 = sorted(tridict.items(),key=takeSecond,reverse=True)[:20]
    for item in templist1:
        bigram_global[item[0]]=item[1]
    
    for item in templist2:
        trigram_global[item[0]]=item[1]
    
    for items in bigram_global.keys():
        n_grams_40.append(items)

    for items in trigram_global.keys():
        n_grams_40.append(items)
    

def main():
    n_grams()
    data = pd.read_csv('./files/3_govt_urls_state_only.csv')
    data = data['Note']
    
    with open('n_output.csv','w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(["Topic","Note"])
        for item in data:
            note = item.split("--")[0]
            nostopword_note = ' '.join(stopwordsremover(note))
            for i in range(2,4):
                n_gram = ngramchecker(nostopword_note,i)
                for item in n_gram:
                    if item in n_grams_40:
                        writer.writerow([f"{item}",f"{note}"])


main()